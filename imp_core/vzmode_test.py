from datetime import datetime
import time
import sys, time, threading, abc, signal
from threading import Event

from paho.mqtt import client as mqtt_client
import paho.mqtt.subscribe as mqtt_subscribe

from .routed_msg import georoutedmsg_pb2

import requests
import json

spat_data = [
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x00P\x00\x82(\x00\x01\xc0',
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x00H\x00\x82(\x00\x01\x80',
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x00@\x00\x82(\x00\x01@',
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x008\x00\x82(\x00\x01\x00',
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x000\x00\x82(\x00\x00\xc0',
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x00(\x00\x82(\x00\x00\x80',
    b'\x00\x13\x14\x00\x00\x07\xd4\x82\x04\x00\x01\x00\x00C\x00\x00 \x00\x82(\x00\x00@',
    b'\x00\x13\x14\x00\x00\x07\xd4\x83\x04\x00\x01\x00\x00C\x00\x00\x18\x00\x82@\x00\x00\xc0',
    b'\x00\x13\x14\x00\x00\x07\xd4\x83\x04\x00\x01\x00\x00C\x00\x00\x10\x00\x82@\x00\x00\x80',
    b'\x00\x13\x14\x00\x00\x07\xd4\x83\x04\x00\x01\x00\x00C\x00\x00\x08\x00\x82@\x00\x00@',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x008\x00\x82\x18\x00\x02\x80',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x000\x00\x82\x18\x00\x02@',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x00(\x00\x82\x18\x00\x02\x00',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x00 \x00\x82\x18\x00\x01\xc0',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x00\x18\x00\x82\x18\x00\x01\x80',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x00\x10\x00\x82\x18\x00\x01@',
    b'\x00\x13\x14\x00\x00\x07\xd4\x85\x04\x00\x01\x00\x00E\x00\x00\x08\x00\x82\x18\x00\x01\x00',
    b'\x00\x13\x14\x00\x00\x07\xd4\x86\x04\x00\x01\x00\x00H\x00\x00\x18\x00\x82\x18\x00\x00\xc0',
    b'\x00\x13\x14\x00\x00\x07\xd4\x86\x04\x00\x01\x00\x00H\x00\x00\x10\x00\x82\x18\x00\x00\x80',
    b'\x00\x13\x14\x00\x00\x07\xd4\x86\x04\x00\x01\x00\x00H\x00\x00\x08\x00\x82\x18\x00\x00@',
    ]

class MqttClient(threading.Thread):
    def __init__(self, stop_event):

        super().__init__(group=None, name='vzmode_client_test')
        self.evt = stop_event

        # host_addr = "imp.lite.dltdemo.io"
        host_addr = "vzmode.las.wl.dltdemo.io"
        # host_port = 1883
        host_port = 31234
        entity_id = 38

        self.vzmode_mqtt_client = None
        self.vz_mode_mqtt_broker_address = host_addr
        self.vz_mode_mqtt_broker_port = host_port

        # Pub topics
        self.MQTT_TOPIC_BSM = f"VZCV2X/3/IN/VEH/PSGR/MCAS/entity_id/UPER/BSM"

        self.vzmode_mqtt_client = mqtt_client.Client(client_id="Python-Bsm-Generator")
        self.vzmode_mqtt_client.username_pw_set("adot_user", "9rmcWLxlxe")
        self.vzmode_mqtt_client.on_connect= self.on_connect 
        self.vzmode_mqtt_client.on_message = self.on_message
        self.vzmode_mqtt_client.on_subscribe = self.on_subscribe
        self.vzmode_mqtt_client.on_disconnect = self.on_disconnect
        print("MqttClient Init Complete")

    def get_data_from_file(self, uper_file):
        with open(uper_file, mode='rb') as f:
            encoded_data = f.read()
        return encoded_data
    
    def send_rsa_msg(self):
        pass

    def spat_timer_callback(self):
       
        while(True):
            for i in range(0,20):
                print(f"Sending SPAT... {i:02d}")
                routed_msg = self.getRoutedMsg(spat_data[i])
                msg_info = self.vzmode_mqtt_client.publish(self.MQTT_TOPIC_SPAT, routed_msg, qos=0, retain=False)
                print(f"Publishing to {self.MQTT_TOPIC_SPAT}")
                time.sleep(1)


    def getRoutedMsg(self, bytes_data):
        routed_msg = georoutedmsg_pb2.GeoRoutedMsg()
        routed_msg.msgBytes = bytes_data
        routed_msg.time.FromDatetime(datetime.now())
        routed_msg.position.latitude = 40.5597944       # Derek Place
        routed_msg.position.longitude = -74.8770742     # Derek Place
        ser_msg = routed_msg.SerializeToString()
        return ser_msg

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:    
            print("Connected to VzMode Las")   
            self.send_rsa_msg() 
            # threading.Thread(target=self.spat_timer_callback).start()
        else:
            print("Connection failed")

    def on_disconnect(self, client, userdata, flags, rc):
        print("disconnected")

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
        print("disconnected from IMP")


def register_client():
    
    crs_url = "http://vzmode.las.wl.dltdemo.io:30413/registration"
    client_data = { "ClientInformation":{ "EntityType":"VEH", "EntitySubtype":"PSGR", "VendorID":"MCAS" }, "RSA":{ "MsgFormat":"UPER" }, "PSM":{ "MsgFormat":"UPER" }, "MAP":{ "MsgFormat":"UPER" }, "SPAT":{ "MsgFormat":"UPER" } }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(crs_url, data=json.dumps(client_data), headers=headers)

    print(r.text)   
    # got 38 and 39 as response

def main():
    # register_client()
    print("VzMode las testing")
    
    main_stop_event = Event()
    mqtt_client = MqttClient(main_stop_event)
    # mqtt_client.setDaemon(True)
    mqtt_client.start()

    
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
