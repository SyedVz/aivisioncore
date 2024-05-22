import os
import json
import time

from .imp_platform.imp_client import IMPClient
from .imp_platform.data_types import *

from .imp_platform.data_types import ImageDetection
from .imp_platform.data_types import DetectionExtents
from .imp_platform.data_types import IncidentsName

if __name__ == "__main__":
    print("In Main")
    this_dir = os.path.dirname(__file__)
    root_dir = os.path.dirname(this_dir)
    weights_file = os.path.join(root_dir, "assets", f'{"yolov7"}.pt')

    print(f"this_dir: {this_dir}")
    print(f"thisroot_dir_dir: {root_dir}")
    print(f"weights_file: {weights_file}")

    imp_client = IMPClient("dummy_ip", "dummy_port")

    if (imp_client.is_valid()):
        print("Valid IMP client")
        imp_client.send_incident_detection(IncidentsName.explosion, "CAM1")
        time.sleep(5)
        imp_client.send_incident_detection(IncidentsName.accident, "CAM2")
        time.sleep(5)
        imp_client.send_incident_detection(IncidentsName.accident, "None")
        time.sleep(5)
    else:
        print("Invalid IMP client")