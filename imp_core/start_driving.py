import sys
import os
import socket
import threading
import time
import queue
from .vzmode_interface import MqttVzModeClient
from threading import Event
import argparse


import requests
import json

class MyCar:
    def __init__(self, stop_event, cv_connect=False, route_file_name=None):
        self.localIP     = "127.0.0.1"
        self.localPort   = 6161
        self.bufferSize  = 1024

        self.UDPServerSocket = None
        self.client_addr = self.localIP #temp
        self.client_msg_count = 0
        self.client_available = False

        self.msg_q = queue.Queue()
        self.stop_event = stop_event

        self.loc_input_file = route_file_name

        if (cv_connect):
            # # Create a datagram socket
            self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            # # Bind to address and ip
            self.UDPServerSocket.bind((self.localIP, self.localPort))

        # Class for registering and sending messages to VzMode mqtt
        self.create_mqtt_client()

        if (cv_connect):
            t1 = threading.Thread(target=self.server_cv_listener_thread, daemon=True)  
        t2 = threading.Thread(target=self.update_car_location_thread, daemon=True)  

        if (cv_connect):
            t1.start()  
        t2.start()

        if (cv_connect):
            t1.join()
        t2.join()

    def server_cv_listener_thread(self):
        # Listen for incoming datagrams
        print("UDP server up and listening")
        while(True):

            data, self.client_addr = self.UDPServerSocket.recvfrom(self.bufferSize)
            self.client_available = True
            # clientMsg = "Message from Client:{}".format(data)
            # clientIP  = "Client IP Address:{}".format(self.client_addr)
            # msg = data.decode('utf-8')
            # print(msg)

            if (self.mqtt_client):
                self.mqtt_client.send_message(data)

            time.sleep(0.1)

    def update_car_location_thread(self):
       
       # wait until mqtt is connected
       while(self.mqtt_client.is_connected() != True):
           print("Waiting for MQTT connection")
           time.sleep(1)
           
       print("MQTT connected. Start to send BSMs...")
       self.mqtt_client.publish_bsm()

    def create_mqtt_client(self):

        # First register to get the client ID
        client_id = self.register_client()

        # Creation of this client also starts sending BSMs messages
        self.mqtt_client = MqttVzModeClient(self.stop_event, client_id, thread_name="vzmode_veh_car1", location_file=self.loc_input_file)

         # mqtt_client.setDaemon(True)
        self.mqtt_client.start()

    def register_client(self) -> int:
    
        client_entity_id = 0
        vz_mode_crs_url = "http://vzmode.nyc.wl.dltdemo.io:30413/registration"

        try:
            client_data = { "ClientInformation":{ "EntityType":"VEH", "EntitySubtype":"PSGR", "VendorID":"MCAS" }, "BSM":{ "MsgFormat":"UPER" }, "RSA":{ "MsgFormat":"UPER" }, "PSM":{ "MsgFormat":"UPER" }, "MAP":{ "MsgFormat":"UPER" }, "SPAT":{ "MsgFormat":"UPER" } }
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            r = requests.post(vz_mode_crs_url, data=json.dumps(client_data), headers=headers)
            js = json.loads(r.text)
            client_entity_id = js.get('ID') # the json response is of format {"ID": 9}
            print("Registration of Client successful...")
            print(f"Entity ID is: {client_entity_id}")

        except:
            print("Failed to register the vzmode client")

        return client_entity_id

def main(args): 
    try:
        main_stop_event = Event()
        route_file_name = get_route_file_name(args.route)
        print(f"Route File is: {route_file_name}")
        my_car = MyCar(main_stop_event, args.cv_connect, route_file_name)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)

def get_route_file_name(loc_input=None)->str:
    route_file_name = None
    if (loc_input):
        if (loc_input == "1" or loc_input == "r1" or loc_input=="route1"):
            route_file_name = "imp_core/vz_data/routes_1.csv"
        elif (loc_input == "2" or loc_input == "r2" or loc_input=="route2"):
            route_file_name = "imp_core/vz_data/routes_2.csv"
        elif (loc_input == "3" or loc_input == "r3" or loc_input=="route3"):
            route_file_name = "imp_core/vz_data/routes_3.csv"
        elif (loc_input == "4" or loc_input == "r4" or loc_input=="route4"):
            route_file_name = "imp_core/vz_data/routes_4.csv"

    return route_file_name

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Drive Car. Send BSM messages of its location')
    parser.add_argument('--cv_connect', action='store_true',help='Listen to CV messages')
    parser.add_argument('-r', '--route', type=str, help='Route Number', required=False)
    args = parser.parse_args()
    print(f"cv_connect is : {args.cv_connect}")

    main(args)