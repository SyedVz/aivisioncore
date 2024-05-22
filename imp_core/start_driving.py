import socket
import threading
import time
import queue
from .vzmode_interface import MqttVzModeClient
from threading import Event

import requests
import json

class MyCar:
    def __init__(self, stop_event):
        self.localIP     = "127.0.0.1"
        self.localPort   = 6161
        self.bufferSize  = 1024

        self.UDPServerSocket = None
        self.client_addr = self.localIP #temp
        self.client_msg_count = 0
        self.client_available = False

        self.msg_q = queue.Queue()
        self.stop_event = stop_event

        # Create a datagram socket
        self.UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        self.UDPServerSocket.bind((self.localIP, self.localPort))

        # Class for registering and sending messages to IMP mqtt
        self.create_mqtt_client()

        t1 = threading.Thread(target=self.server_thread)        
        t1.start()
        t1.join()

    def server_thread(self):
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

    def create_mqtt_client(self):

        # First register to get the client ID
        client_id = self.register_client()

        # Creation of this client also starts sending BSMs messages
        self.mqtt_client = MqttVzModeClient(self.stop_event, client_id)

         # mqtt_client.setDaemon(True)
        self.mqtt_client.start()

    def register_client(self) -> int:
    
        client_entity_id = 0
        vz_mode_crs_url = "http://vzmode.las.wl.dltdemo.io:30413/registration"

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
    

def main(): 
    main_stop_event = Event()
    my_car = MyCar(main_stop_event)


if __name__ == '__main__':
    main()