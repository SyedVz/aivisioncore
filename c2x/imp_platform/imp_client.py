from .data_types import ImageDetection
from .data_types import DetectionExtents
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
            detected_object = type.__str__
          
        if (self.UDPClientSocket) :
            self.UDPClientSocket.sendto(str.encode(detected_object), self.serverAddressPort)

        return True