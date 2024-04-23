import socket
import threading
import time
import queue
from .imp_publishser import MqttClient
from threading import Event

class UDPServer:
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
        self.mqtt_client = MqttClient(self.stop_event)

         # mqtt_client.setDaemon(True)
        self.mqtt_client.start()

def main(): 
    main_stop_event = Event()
    udpServer = UDPServer(main_stop_event)


if __name__ == '__main__':
    main()