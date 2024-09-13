from paho.mqtt import client as mqtt_client
import paho.mqtt.subscribe as mqtt_subscribe
import time
from datetime import datetime, timedelta, timezone
import mycodec as mycodec
import json
import queue
from collections import deque

import sys, time, threading, abc, signal
from threading import Event
from google.protobuf import timestamp_pb2

import imp_core.routed_msg_vzmode.routed_msg_pb2 as routed_msg_pb2
from .rsa_msg_helper import Rsa_Helper
from .location_helper import Location_Helper

ItisTypes = Rsa_Helper.ItisTypes

default_entity_id = 200             # Used if not registering the client

class MqttVzModeClient(threading.Thread):
    def __init__(self, stop_event, client_id=0, thread_name="vzmode_rsu", location_file=None):

        super().__init__(group=None, name=thread_name)
        self.evt = stop_event
        self.msg_q = queue.Queue()

        if (client_id != 0):
            self.entity_id = client_id
        else:
            self.entity_id =  default_entity_id

        self.vzmode_mqtt_client = None
        self.vz_mode_mqtt_broker_address = "vzmode.nyc.wl.dltdemo.io"
        self.vz_mode_mqtt_broker_port = 31234
        self.vz_mode_mqtt_is_connected = False
        self.vz_mode_crs_url = "http://vzmode.nyc.wl.dltdemo.io:30413/registration"

        # Pub topics
        self.MQTT_BSM_UPER = f"VZCV2X/3/IN/VEH/PSGR/MCAS/{self.entity_id}/UPER/BSM"
        self.MQTT_RSA = "VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD"

        # Sub Topics
        self.MQTT_RSA_SUB = f"VZCV2X/3/OUT/VEH/PSGR/MCAS/{self.entity_id}/UPER/RSA"
        self.MQTT_RSA_EMER_SUB = f"VZCV2X/3/OUT/VEH/PSGR/MCAS/{self.entity_id}/UPER/RSA_EMER"

        self.vzmode_mqtt_client = mqtt_client.Client(client_id=f"VEH-{self.entity_id}")
        self.vzmode_mqtt_client.username_pw_set("adot_user", "9rmcWLxlxe")
        self.vzmode_mqtt_client.on_connect = self.on_connect
        self.vzmode_mqtt_client.on_message = self.on_message
        self.vzmode_mqtt_client.on_subscribe = self.on_subscribe
        self.vzmode_mqtt_client.on_disconnect = self.on_disconnect

        google_route_available = False
        if(location_file): 
            google_route_available = True
        self.location_helper = Location_Helper(stop_event, route_file=location_file, google_route=google_route_available)

        # Load BSM data from file
        # self.saved_car_route = None
        # self.saved_car_route_2 = None
        # self.saved_car_route_len = 0

        # self.telemetry_file = "telemetry_input_arizona.csv"

        # with open (self.telemetry_file) as f:
        #     self.saved_car_route = f.readlines()
        #     del self.saved_car_route[0]    # Delete the row with col titles
        #     self.saved_car_route_len = len(self.saved_car_route)
        #     dq = deque(self.saved_car_route)
        #     # dq.rotate(500)                 # Just rotate the data to use for the second car
        #     self.saved_car_route_2 = list(dq)

        print("MqttVzModeClient Init Complete")

    def send_message(self, msg):
        self.msg_q.put(msg)

    def genAI_CV2X_msg_loop(self):
        while(True):
            try:
                msg = self.msg_q.get(timeout=1.0/60)
                if (self.vz_mode_mqtt_is_connected):
                    # print(f"Processing msg: {msg}")
                    self.process_genAI_CV2X_msgs(msg)
                else:
                    print(f"GenAI message {msg} But IMP not connected")
                # Publish this message based on its type etc
            except queue.Empty:
                # print("Empty message queue")
                pass
            except Exception as e:
                print(f"Error processing message queue {e}")
        
            time.sleep(0.1) 

    def process_genAI_CV2X_msgs(self, msg):
        json_str = msg.decode('utf-8')
        jsob_obj = json.loads(json_str)

        cam_pos = jsob_obj.get('cam_pos', None)

        if (not cam_pos):
            cam_pos = {}
            # it means its in car. Need to get location info
            cam_pos['lat_start'] =  self.location_helper.lat + 20
            cam_pos['long_start'] =  self.location_helper.long + 20
            cam_pos['lat_end'] =  self.location_helper.lat - 20
            cam_pos['long_end'] =  self.location_helper.long -20

        incident = jsob_obj.get('Incident', '')

        rsa_id = "AI Incident: "
        if (incident == "explosion"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_explosion
        elif (incident == "accident"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_accident
        elif (incident == "fogwarning"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_fog
        elif (incident == "congestion"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_congestion
        elif (incident == "violation"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_violation
        elif (incident == "construction zone"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_construction
        elif (incident == "custom_incident_1"):
            rsa_id = rsa_id + incident
            itis_codes = ItisTypes.type_custom_incident_1
        else:
            rsa_id = rsa_id + "Advisory"
            itis_codes = ItisTypes.type_none

        # print(cam_pos)
        # print(incident)
        print(f"Setting RSA line for the incident: {incident}")
        self.publish_rsa(rsa_id, rsa_id, cam_pos, itis_codes)

    def is_connected(self):
        return self.vz_mode_mqtt_is_connected

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to NYC Vzmode")
            self.vz_mode_mqtt_is_connected = True
            # threading.Thread(target=self.publish_bsm).start()
            self.vzmode_mqtt_client.subscribe(self.MQTT_RSA_SUB, 0)
            self.vzmode_mqtt_client.subscribe(self.MQTT_RSA_EMER_SUB, 0)
        else:
            print("Connection failed")

    def on_disconnect(self, client, userdata, flags):
        print("disconnected")
        self.vz_mode_mqtt_is_connected = False

    def on_subscribe(self, mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " + str(mid) + " " + str(granted_qos))

    def on_message(self, mosq, obj, msg):
        # print("Message received")
        # print("Topic: " + str(msg.topic))
        # print("QoS: " + str(msg.qos))
        # print("Payload: " + str(msg.payload))
        msg_type = self.message_type(str(msg.topic)).upper()
        if (msg_type == "BSM"):
            sys.stdout.write(".")
            sys.stdout.flush()
        elif (msg_type == "RSA"):
            print()
            print(f"RSA message received{str(msg.topic)}") 
        else:
            print()
            print(str(msg.topic))   

    def message_type(self, topic) -> str:
        arr = topic.split("/")
        return arr[-1]
    
    def run(self):
        try:

             # Start a thread to process incoming messages from GenAI
            threading.Thread(target=self.genAI_CV2X_msg_loop).start()

            # Connect to VzMode
            self.vzmode_mqtt_client.connect(self.vz_mode_mqtt_broker_address, port=self.vz_mode_mqtt_broker_port)  # connect to broker
            self.vzmode_mqtt_client.loop_start()  # start the loop

        except ConnectionResetError:
            print("Error: connection has been reset")
            pass

        self.location_helper.start()

        self.evt.wait()
        self.vzmode_mqtt_client.disconnect()
        print("disconnected from VzMode")

    def publish_bsm(self):
       # Continously publish the bsm data
        while (True):
            routed_msg = self.get_bsm_message()
            token = self.vzmode_mqtt_client.publish(self.MQTT_BSM_UPER, routed_msg, qos=0, retain=False)
            # print(f"\rPublished: Token is: {token}")
            sys.stdout.write(f"\rPublished: Token is: {token}")
            time.sleep(0.1)

    def publish_rsa(self, rsa_id:str, rsa_desc:str, rsa_pos, itis_codes:ItisTypes):
        rsa_helper = Rsa_Helper()
        ser_msg = rsa_helper.get_rsa_message(rsa_id, rsa_desc, rsa_pos, itis_codes) 
        print(ser_msg)
        
        # now publish your message (denoted by 'bytes') to VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD
        token = self.vzmode_mqtt_client.publish(self.MQTT_RSA, ser_msg, qos=0, retain=False)
        print(f"Published: Token is: {token}")

    def get_bsm_message(self):
        id = "%0.8X" % self.entity_id
        # base bsm_msg to build the actual message from
        bsm_msg = {"messageId": 20, "value": {"coreData": {"msgCnt": 34, "id": id, "secMark": 36618, "lat": 373815394, "long": -1219919597, "elev": -4096, "accuracy": {"semiMajor": 255, "semiMinor": 255, "orientation": 65535}, "transmission": "unavailable", "speed": 0, "heading": 24165, "angle": 127, "accelSet": {"long": 2001, "lat": 2001, "vert": -127, "yaw": 0}, "brakes": {"wheelBrakes": {"length": 5, "value": "00"}, "traction": "unavailable", "abs": "unavailable", "scs": "unavailable", "brakeBoost": "unavailable", "auxBrakes": "unavailable"}, "size": {"width": 200, "length": 599}}}}

        bsm_msg["value"]["coreData"]["msgCnt"] = self.location_helper.msgCnt
        bsm_msg["value"]["coreData"]["lat"] = self.location_helper.lat
        bsm_msg["value"]["coreData"]["long"] = self.location_helper.long
        bsm_msg["value"]["coreData"]["elev"] = self.location_helper.elev
        bsm_msg["value"]["coreData"]["speed"] = self.location_helper.speed_bsm
        bsm_msg["value"]["coreData"]["heading"] = self.location_helper.heading
        # print(bsm_msg["value"]["coreData"])

        encoded_bsm = encode(bsm_msg)
        routed_msg = self.getRoutedMsg(bytes(encoded_bsm), self.location_helper.lat, self.location_helper.long)

        return routed_msg

    def get_bsm_message_2_old(self, msg_type:str):
        if (msg_type == 'jer'):
            bsm_msg_jer_1 = '{"MessageFrame": {"messageId": "20", "value": {"BasicSafetyMessage": {"partII": {"PartIIcontent": [{"partII-Id": "0", "partII-Value": {"VehicleSafetyExtensions": {"events": "0000000000000", "lights": "000000000"}}}, {"partII-Id": "1", "partII-Value": {"SpecialVehicleExtensions": {"vehicleAlerts": {"sirenUse": {"notInUse": ""}, "lightsUse": {"notInUse": ""}, "multi": {"unavailable": ""}, "sspRights": "0"}}}}]}, "coreData": {"secMark": "41868", "lat": "405597944", "accuracy": {"semiMajor": "1", "semiMinor": "1", "orientation": "65534"}, "id": "00 00 00 00", "long": "-748770742", "transmission": {"neutral": ""}, "size": {"width": "246", "length": "619"}, "speed": "375", "accelSet": {"long": "-2", "lat": "0", "vert": "0", "yaw": "2443"}, "brakes": {"scs": {"unavailable": ""}, "brakeBoost": {"unavailable": ""}, "auxBrakes": {"unavailable": ""}, "wheelBrakes": "00000", "traction": {"unavailable": ""}, "abs": {"unavailable": ""}}, "msgCnt": "40", "elev": "464", "heading": "14471", "angle": "0"}}}}}'
            
            bsm_msg_jer_2 = '{"messageId": 20, "value": {"coreData": {"msgCnt": 34, "id": "30626A5A", "secMark": 36618, "lat": 373815394, "long": -1219919597, "elev": -4096, "accuracy": {"semiMajor": 255, "semiMinor": 255, "orientation": 65535}, "transmission": "unavailable", "speed": 0, "heading": 24165, "angle": 127, "accelSet": {"long": 2001, "lat": 2001, "vert": -127, "yaw": 0}, "brakes": {"wheelBrakes": {"length": 5, "value": "00"}, "traction": "unavailable", "abs": "unavailable", "scs": "unavailable", "brakeBoost": "unavailable", "auxBrakes": "unavailable"}, "size": {"width": 200, "length": 599}}}}'
            routed_msg = self.getRoutedMsg(bsm_msg_jer_1.encode("utf-8"))
            return bsm_msg_jer_1
        else:
            bsm_msg = None
            with open ("bsm.uper", "rb") as f:
                bsm_msg = f.read()
            routed_msg = self.getRoutedMsg(bsm_msg)
            return routed_msg

    def getRoutedMsg(self, bytes_data, lat=405597944, long=-748770742):
        routed_msg = routed_msg_pb2.RoutedMsg()
        routed_msg.msgBytes = bytes_data
        routed_msg.time.FromDatetime(datetime.now())
        routed_msg.position.latitude = lat
        routed_msg.position.longitude = long
        ser_msg = routed_msg.SerializeToString()
        return ser_msg

def encode(json_data = None) -> bytearray:
    encoded = None
    try:
        violations = mycodec.DSRC.MessageFrame.validate(json_data)
        encoded = mycodec.DSRC.MessageFrame.encode('UPER', json_data)
        # print('Encoded HEX: ' + ', '.join(['0x{:02X}'.format(val) for val in encoded]))
        # print()

    except NotImplementedError as e:
        print('Not Implemented Error : {}'.format(format(e)))

    return encoded

