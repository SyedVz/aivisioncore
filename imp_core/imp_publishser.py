from datetime import datetime
import json
import time
import sys, time, threading, abc, signal
from threading import Event
import queue

from paho.mqtt import client as mqtt_client
import json
import paho.mqtt.subscribe as mqtt_subscribe

from routed_msg import georoutedmsg_pb2

class MqttIMPClient(threading.Thread):
    def __init__(self, stop_event):

        super().__init__(group=None, name='imp_mqtt_client_test')
        self.evt = stop_event
        self.msg_q = queue.Queue()
        self.imp_connected = False

        self.vzmode_mqtt_client = None
        self.vz_mode_mqtt_broker_address = "imp.lite.dltdemo.io"
        self.vz_mode_mqtt_broker_port = 1883

        # Pub topics
        self.MQTT_TOPIC_BSM = "vzimp/1/Regional/d/r/4/z/x/z/6/x/p/TRAFLT/NA/genAI_cv2x/JER/BSM"
        self.MQTT_TOPIC_PSM = "vzimp/1/Regional/d/r/4/z/x/z/6/x/p/TRAFLT/NA/genAI_cv2x/JER/PSM"
        self.MQTT_TOPIC_RSA = "vzimp/1/Regional/d/r/4/z/x/z/6/x/p/TRAFLT/NA/genAI_cv2x/JER/RSA"
        self.MQTT_TOPIC_TIM = "vzimp/1/Regional/d/r/4/z/x/z/6/x/p/TRAFLT/NA/genAI_cv2x/JER/TIM"

        self.vzmode_mqtt_client = mqtt_client.Client(client_id="GenAICV2X")
        self.vzmode_mqtt_client.username_pw_set("auto", "test")
        self.vzmode_mqtt_client.on_connect= self.on_connect 
        self.vzmode_mqtt_client.on_message = self.on_message
        self.vzmode_mqtt_client.on_subscribe = self.on_subscribe
        self.vzmode_mqtt_client.on_disconnect = self.on_disconnect
        print("MqttIMPClient Init Complete")

    def send_message(self, msg):
        self.msg_q.put(msg)

    def genAI_CV2X_msg_loop(self):
        while(True):
            try:
                msg = self.msg_q.get(timeout=1.0/60)
                if (self.imp_connected):
                    print(f"Processing msg: {msg}")
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
        pass

    def getRoutedMsg(self, bytes_data):
        routed_msg = georoutedmsg_pb2.GeoRoutedMsg()
        routed_msg.msgBytes = bytes_data
        routed_msg.time.FromDatetime(datetime.now())
        routed_msg.position.latitude = 407344084
        routed_msg.position.longitude = -745384722
        ser_msg = routed_msg.SerializeToString()
        return ser_msg

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:    
            print("Connected to IMP Lite")  
            self.imp_connected = True  
        else:
            print("Connection failed")

    def on_disconnect(self, client, userdata, flags, rc):
        print("disconnected")
        self.imp_connected = False

    def on_subscribe(self, mosq, obj, mid, granted_qos):
        print("Subscribed to Topic: " + str(granted_qos))

    def on_message(self, mosq, obj, msg):
        print("Message received")
        print("Topic: " + str(msg.topic))
        #print("QoS: " + str(msg.qos))
        #print("Payload: " + str(msg.payload))
        
        # TODO - Dont decode now
        # decoded_message = self.parse_msg(msg.payload)
        # print(decoded_message)

    def parse_msg(self, msg):
        routed_msg = georoutedmsg_pb2.GeoRoutedMsg()        
        routed_msg.ParseFromString(msg)
        data_bytes = routed_msg.msgBytes

        data_str = None
        json_data = None

        try:
            data_str = data_bytes.decode("utf-8")
            decoded_data = json.loads(data_str)
        except:
            print("Cannot decode the payload as string")
            print("Trying it as Uper")
            try:
                decoded_data = decode(data_bytes) # TODO this is not available as of now
            except:
                print("Cannot decode the payload as UPER as well")

        return decoded_data

    def run(self):
        try:
            # Start a thread to process incoming messages from GenAI
            threading.Thread(target=self.genAI_CV2X_msg_loop).start()

            # Connect to IMP
            self.vzmode_mqtt_client.connect(self.vz_mode_mqtt_broker_address, port=self.vz_mode_mqtt_broker_port)          #connect to broker
            self.vzmode_mqtt_client.loop_start()        #start the loop

        except ConnectionResetError:
            print("Error: connection has been reset")
            pass
        
        self.evt.wait()        
        self.vzmode_mqtt_client.disconnect()
        print("disconnected from IMP")

def decode(encoded: bytearray) -> str:

    decoded =  None

    try:

        if encoded:
            print('Decoding "DSRC.MessageFrame":')
            decoded = mycodec.DSRC.MessageFrame.decode('UPER', encoded)

            print('Decoded value: {}'.format(json.dumps(decoded, default=str)))
            print()

            print('Validating "DSRC.MessageFrame":')

            # the 'field reference' property can be used with a tool implementing the JSON Pointer spec
            violations = mycodec.DSRC.MessageFrame.validate(decoded)

            print('Constraint violations: {}'.format(json.dumps(violations, default=str)))
            print()
        else:
            print("Couldn't open uper file or its empty")
                  
    except NotImplementedError as e:
        print('Not Implemented Error : {}'.format(format(e)))
    
    return decoded

