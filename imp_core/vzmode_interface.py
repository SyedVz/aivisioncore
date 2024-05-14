from paho.mqtt import client as mqtt_client
import paho.mqtt.subscribe as mqtt_subscribe
import time
from datetime import datetime, timedelta, timezone
import mycodec as mycodec
import json
from collections import deque

import sys, time, threading, abc, signal
from threading import Event
from google.protobuf import timestamp_pb2

import routed_msg_pb2
from .rsa_msg_helper import Rsa_Helper
from .location_helper import Location_Helper


class MqttVzModeClient(threading.Thread):
    def __init__(self, stop_event):

        super().__init__(group=None, name="vzmode_python_mkz_car")
        self.evt = stop_event

        self.vzmode_mqtt_client = None
        self.vz_mode_mqtt_broker_address = "vzmode.las.wl.dltdemo.io"
        self.vz_mode_mqtt_broker_port = 31234
        self.vz_mode_mqtt_is_connected = False

        # Pub topics
        self.MQTT_BSM_UPER = "VZCV2X/3/IN/VEH/PSGR/MCAS/200/UPER/BSM"
        self.MQTT_RSA = "VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD"

        self.vzmode_mqtt_client = mqtt_client.Client(client_id="adot_python_user")
        self.vzmode_mqtt_client.username_pw_set("adot_user", "9rmcWLxlxe")
        self.vzmode_mqtt_client.on_connect = self.on_connect
        self.vzmode_mqtt_client.on_message = self.on_message
        self.vzmode_mqtt_client.on_subscribe = self.on_subscribe
        self.vzmode_mqtt_client.on_disconnect = self.on_disconnect

        self.location_helper = Location_Helper(stop_event)

        # Load BSM data from file
        self.saved_car_route = None
        self.saved_car_route_2 = None
        self.saved_car_route_len = 0

        self.telemetry_file = "telemetry_input_arizona.csv"

        with open (self.telemetry_file) as f:
            self.saved_car_route = f.readlines()
            del self.saved_car_route[0]    # Delete the row with col titles
            self.saved_car_route_len = len(self.saved_car_route)
            dq = deque(self.saved_car_route)
            # dq.rotate(500)                 # Just rotate the data to use for the second car
            self.saved_car_route_2 = list(dq)

        print("MqttVzModeClient Init Complete")

    def is_connected(self):
        return self.vz_mode_mqtt_is_connected

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to LAS Vzmode")
            self.vz_mode_mqtt_is_connected = True
            threading.Thread(target=self.publish_bsm).start()
        else:
            print("Connection failed")

    def on_disconnect(self, client, userdata, flags, rc):
        print("disconnected")
        self.vz_mode_mqtt_is_connected = False

    def on_subscribe(self, mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " + str(granted_qos))

    def on_message(self, mosq, obj, msg):
        print("Message received")
        print("Topic: " + str(msg.topic))
        # print("QoS: " + str(msg.qos))
        # print("Payload: " + str(msg.payload))

    def run(self):
        try:

            self.vzmode_mqtt_client.connect(
                self.vz_mode_mqtt_broker_address, port=self.vz_mode_mqtt_broker_port
            )  # connect to broker
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
            print(f"Published: Token is: {token}")
            time.sleep(0.1)

    def publish_rsa(self):
        ser_msg = Rsa_Helper.get_rsa_message() 
        print(ser_msg)
        
        # now publish your message (denoted by 'bytes') to VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD
        token = self.vzmode_mqtt_client.publish(self.MQTT_RSA, ser_msg, qos=0, retain=False)
        print(f"Published: Token is: {token}")

    def get_bsm_message(self):
        # base bsm_msg to build the actual message from
        bsm_msg = {"messageId": 20, "value": {"coreData": {"msgCnt": 34, "id": "000000C8", "secMark": 36618, "lat": 373815394, "long": -1219919597, "elev": -4096, "accuracy": {"semiMajor": 255, "semiMinor": 255, "orientation": 65535}, "transmission": "unavailable", "speed": 0, "heading": 24165, "angle": 127, "accelSet": {"long": 2001, "lat": 2001, "vert": -127, "yaw": 0}, "brakes": {"wheelBrakes": {"length": 5, "value": "00"}, "traction": "unavailable", "abs": "unavailable", "scs": "unavailable", "brakeBoost": "unavailable", "auxBrakes": "unavailable"}, "size": {"width": 200, "length": 599}}}}

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

