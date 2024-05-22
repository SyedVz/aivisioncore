from paho.mqtt import client as mqtt_client
import paho.mqtt.subscribe as mqtt_subscribe
import time
from datetime import datetime, timedelta, timezone


import sys, time, threading, abc, signal
from threading import Event

import imp_core.routed_msg_vzmode.routed_msg_pb2 as routed_msg_pb2
from google.protobuf import timestamp_pb2


class MqttClient(threading.Thread):
    def __init__(self, stop_event):

        super().__init__(group=None, name='vzmode_python_setrsa_client')
        self.evt = stop_event

        self.vzmode_mqtt_client = None
        self.vz_mode_mqtt_broker_address = "vzmode.las.wl.dltdemo.io"
        self.vz_mode_mqtt_broker_port = 31234

        # Pub topics
        self.MQTT_BSM = "VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD"  
        self.MQTT_RSA = "VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD"
        
        self.vzmode_mqtt_client = mqtt_client.Client(client_id="adot_python_user")
        self.vzmode_mqtt_client.username_pw_set("adot_user", "9rmcWLxlxe")
        self.vzmode_mqtt_client.on_connect= self.on_connect 
        self.vzmode_mqtt_client.on_message = self.on_message
        self.vzmode_mqtt_client.on_subscribe = self.on_subscribe
        self.vzmode_mqtt_client.on_disconnect = self.on_disconnect
        print("MqttClient Init Complete")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:    
            print("Connected to LAS Vzmode")   
            self.publish_rsa()
            # All done. Now disconnect
            self.vzmode_mqtt_client.disconnect()
        else:
            print("Connection failed")

    def on_disconnect(self, client, userdata, flags):
        print("MQTT disconnected")
        print("Exiting...")
        self.vzmode_mqtt_client.loop_stop()
        self.evt.set()

    def on_subscribe(self, mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " + str(granted_qos))

    def on_message(self, mosq, obj, msg):
        print("Message received")
        print("Topic: " + str(msg.topic))
        #print("QoS: " + str(msg.qos))
        #print("Payload: " + str(msg.payload))

    def run(self):
        try:
        
            self.vzmode_mqtt_client.connect(self.vz_mode_mqtt_broker_address, port=self.vz_mode_mqtt_broker_port)          #connect to broker
            self.vzmode_mqtt_client.loop_start()        #start the loop

        except ConnectionResetError:
            print("Error: connection has been reset")
            pass
        
        self.evt.wait()        
        self.vzmode_mqtt_client.disconnect()
        print("disconnected from VzMode")
        
    def publish_rsa(self):
        ser_msg = get_rsa_message() 
        print(ser_msg)
        
        # now publish your message (denoted by 'bytes') to VZCV2X/3/IN/SW/NA/ADOT/0/JER/AUTOPUB_ADD
        token = self.vzmode_mqtt_client.publish(self.MQTT_RSA, ser_msg, qos=0, retain=False)
        print(f"Published: Token is: {token}")
        
def get_rsa_message() -> bytes:
    #  I don't know the best location to store these as static strings in your Go project.
    #  I left them here for simplicity but they should probably be in a safer, more remote
    #  location, along with any other line crossing RSA messages that you want to send.

    #  ****** Reduced Speed Ahead Slow Down ******
    jsonRsa1 = '''
    {
        "MessageFrame":{
            "messageId":"27",
            "value":{
                "RoadSideAlert":{
                    "msgCnt":"0",
                    "timeStamp":"0",
                    "typeEvent":261,
                    "description":{
                        "ITIScodes": ["12302", "268", "13569", "7201"]
                    }
                }
            }
        } 
    }
    
    '''

    # Check document(J2540_2) page 215 for examples of proper encoding

    # ****** Slow Traffic Ahead Proceed With Caution ******
    # jsonRsa2 = 
    # {
    #     "MessageFrame":{
    #         "messageId":"27",
    #         "value":{
    #             "RoadSideAlert":{
    #                 "msgCnt":"0",
    #                 "timeStamp":"0",
    #                 "typeEvent":261,
    #                 "description":{
    #                     "ITIScodes": ["259", "13569", "7714", "12330"]
    #                 }
    #             }
    #         }
    #     }
    # }

    # ****** Delay 10 Minute Delay Interstate 10 Westbound Traffic ******
    # jsonRsa3 = 
    # {
    #     "MessageFrame":{
    #         "messageId":"27",
    #         "value":{
    #             "RoadSideAlert":{
    #                 "msgCnt":"0",
    #                 "timeStamp":"0",
    #                 "typeEvent":261,
    #                 "description":{
    #                     "ITIScodes": ["1537", "12554", "8728", "1537", "11781", "12554", "7997"]
    #                 }
    #             }
    #         }
    #     }
    # }


    # var p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 int32 = 0,0,0,0,0,0,0,0,0,0,0,0
    p0, p1, p2, p3 = 0, 0, 0, 0

    # lineId = "inrixIncidentID_1"
    # endPoints = [4]int32 {p0, p1, p2, p3}
    # setRsaLine (lineId, endPoints, jsonRsa1)

    # lineId = "inrixIncidentID_2"
    # endPoints = [4]int32 {p4, p5, p6, p7}
    # setRsaLine (lineId, endPoints, jsonRsa2)

    # lineId = "inrixIncidentID_3"
    # endPoints = [4]int32 {p8, p9, p10, p11}
    # setRsaLine (lineId, endPoints, jsonRsa3)

    # lineId = "Test_IncidentID_1"
    # p0 = 334800020
    # p1 = -1120383930
    # p2 = 334799823
    # p3 = -1120382324
    # endPoints := [4]int32 {p0, p1, p2, p3}
    # setRsaLine (lineId, endPoints, jsonRsa1)
    
    lineId = "Road_Incident_3"

    cam0_pos = {"lat_start":334800130, "long_start":-1120386210, "lat_end": 334800200, "long_end": -1120381860}
    cam1_pos = {"lat_start":334818970, "long_start":-1120391350, "lat_end": 334819350, "long_end": -1120387270}
    cam2_pos = {"lat_start":334758540, "long_start":-1120386960, "lat_end": 334758470, "long_end": -1120383050}
    cam3_pos = {"lat_start":334746880, "long_start":-1120388250, "lat_end": 334746750, "long_end": -1120383210}

    # p0 = 334800130
    # p1 = -1120386210
    # p2 = 334800200
    # p3 = -1120381860

    cam_pos = cam3_pos

    p0 = cam_pos['lat_start']
    p1 = cam_pos['long_start']
    p2 = cam_pos['lat_end']
    p3 = cam_pos['long_end']

    endPoints = [p0, p1, p2, p3]
    return setRsaLine(lineId, endPoints, jsonRsa1)
    
def setRsaLine(lineId:str, endPoints, jsonRsa:str) -> bytes:

    now_time = datetime.now()
    # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
    msg_end_time = now_time + timedelta(minutes=5) 
     
    # utc_now_time = now_time.replace(tzinfo=timezone.utc)
    # utc_msg_end_time = msg_end_time.replace(tzinfo=timezone.utc)
 
    seconds_now = int(now_time.timestamp())
    seconds_end = int(msg_end_time.timestamp())
     
    nanos_now = int(now_time.timestamp() % 1e9 )
    nanos_end = int(msg_end_time.timestamp() % 1e9)
     
    print("Original")
    print(f"Full: {now_time} Seconds: {seconds_now} Nano: {int()}")
    print(f"Full: {msg_end_time} Seconds: {seconds_end} Nano: {msg_end_time.strftime(('%s'))}")
     
    print("Nanos")
    print(f"Nanos now: {nanos_now}")
    print(f"Nanos now: {nanos_end}")
     
    autoPubAddMsg1 = routed_msg_pb2.AutoPublishAddMsg()
    autoPubAddMsg1.msgBytes = bytes(jsonRsa, 'utf-8')
    autoPubAddMsg1.msgType = "RSA"
    autoPubAddMsg1.id = str(lineId)
    autoPubAddMsg1.description = lineId
    autoPubAddMsg1.entityTypes.MergeFrom(["VEH"])
    autoPubAddMsg1.startTime.MergeFrom(timestamp_pb2.Timestamp(seconds=int(now_time.timestamp()), nanos=int(now_time.timestamp() % 1e9)))
    autoPubAddMsg1.endTime.MergeFrom(timestamp_pb2.Timestamp(seconds=int(msg_end_time.timestamp()), nanos=int(msg_end_time.timestamp() % 1e9)))
    lineCrossing = routed_msg_pb2.LineCrossing()
    lineCrossing.endpoint1.latitude = endPoints[0]
    lineCrossing.endpoint1.longitude = endPoints[1]
    lineCrossing.endpoint2.latitude = endPoints[2]
    lineCrossing.endpoint2.longitude = endPoints[3]
    lineCrossing.roadIdentifier = "NA"
    lineCrossing.direction = routed_msg_pb2.LineCrossing().Direction.Undefined
     
    autoPubAddMsg1.lineCrossingOpt.MergeFrom(lineCrossing)

    # serialize your message
    ser_msg = autoPubAddMsg1.SerializeToString()

    return ser_msg

def main():

    main_stop_event = Event()
    mqtt_client = MqttClient(main_stop_event)
    # mqtt_client.setDaemon(True)
    mqtt_client.start()
    

if __name__ == "__main__":
    main()