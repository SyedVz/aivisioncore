from .data_types import ImageDetection
from .data_types import DetectionExtents
from .data_types import IncidentsName
import socket

class IMPClient:
    def __init__(self, host, port):
        self.host = "127.0.0.1" #host
        self.port = 6161        #port

        self.serverAddressPort     = (self.host, self.port)
        self.bufferSize  = 1024

        # Create a UDP socket at client side
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    def is_valid(self):
        return True


    def send_image_detection(self, type: ImageDetection, extents: DetectionExtents):
        print(f'Sending image detection: {type} at {extents.x}, {extents.y}, {extents.w}, {extents.h}')  

        detected_object = "None"
        if (type):
            detected_object = type.value
           # print('******************************************')
           # print(detected_object)
           # print('******************************************')

        if (self.UDPClientSocket) :
            self.UDPClientSocket.sendto(detected_object.encode(), self.serverAddressPort)

        return True

    def send_incident_detection(self, type :IncidentsName, cameraname):
        print(f'Sending incident detection: {type} ')

        detected_incident = "None"
        if (type):
            detected_incident = type.value


        if (self.UDPClientSocket) :
            self.UDPClientSocket.sendto(detected_incident.encode(), self.serverAddressPort)

        return True