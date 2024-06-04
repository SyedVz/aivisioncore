from .data_types import ImageDetection
from .data_types import DetectionExtents
from .data_types import IncidentsName
import socket
import json

class IMPClient:
    def __init__(self, host, port):
        self.host = host

        self.rsu_port = 7171
        self.car_port = 6161

        self.rsu_address_port     = (self.host, self.rsu_port)
        self.car_address_port     = (self.host, self.car_port)

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

    def send_incident_detection(self, type :IncidentsName, CameraName:str = "None"):
        print(f'Sending incident detection: {type} ')
        print(f'For Camera : {CameraName} ')

        detected_incident = "None"
        if (type):
            detected_incident = type.value

        # if camera is None.. then consider it as a car
        if (CameraName == None or CameraName == "None"):
            server_address_port = self.car_address_port
        else:
            server_address_port = self.rsu_address_port

        cam1_pos = {"lat_start":334818970, "long_start":-1120391350, "lat_end": 334819350, "long_end": -1120387270}
        cam2_pos = {"lat_start":334758540, "long_start":-1120386960, "lat_end": 334758470, "long_end": -1120383050}
        cam3_pos = {"lat_start":334746880, "long_start":-1120388250, "lat_end": 334746750, "long_end": -1120383210}

        if (CameraName == "CAM1"):
            cam_pos = cam1_pos
        elif (CameraName == "CAM2"):
            cam_pos = cam2_pos
        elif (CameraName == "CAM3"):
            cam_pos = cam3_pos
        else:
            cam_pos = {}

        cv_data = {"Incident": detected_incident, "cam_pos": cam_pos}
    
        if (self.UDPClientSocket) :
            self.UDPClientSocket.sendto(json.dumps(cv_data).encode(), server_address_port)

        return True