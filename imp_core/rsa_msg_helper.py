import time
from datetime import datetime, timedelta, timezone
import json
from enum import Enum

import imp_core.routed_msg_vzmode.routed_msg_pb2 as routed_msg_pb2
from google.protobuf import timestamp_pb2

class Rsa_Helper:

    class ItisTypes(Enum):
        type_none = "none"
        type_explosion = 'explosion'
        type_accident = 'accident'
        type_fog = 'fogwarning'
        type_violation = "violation"
        type_construction = "construction"
        type_congestion = "congestion"

        def __str__(self):
            return f'{self.value}'
        
    def __init__(self):
        ItisTypes = self.ItisTypes

    def get_rsa_message(self, rsa_id:str, rsa_desc:str, rsa_pos, itis_type:ItisTypes=ItisTypes.type_none) -> bytes:

        # Check document(J2540_2) page 215 for examples of proper encoding

        # Previous codes
        ITIScodes_Reduced_Speed = ["12302", "268", "13569", "7201"]                     # Reduced Speed Ahead Slow Down
        ITIScodes_Slow_Traffic = ["259", "13569", "7714", "12330"]                      # Slow Traffic Ahead Proceed With Caution
        ITIScodes_Delay = ["1537", "12554", "8728", "1537", "11781", "12554", "7997"]   # Delay 10 Minute Delay Interstate 10 Westbound Traffic

        # New codes for the demo
        ITIScodes_None = ["6922", "7169"]                                               # increased-risk-of-accident drive-carefully 
        ITIScodes_Explosion = ["3102", "8449"]                                          # major-hazardous-materials-fire detour-where-possible 
        ITIScodes_Accident = ["517", "13569", "7443", "7201"]                           # multi-vehicle-accident reduce-your-speed be-prepared-to-stop
        ITIScodes_Fog = ["5383", "7714", "12330"]                                       # visibility-reduced proceed-with caution
        ITIScodes_Violation = ITIScodes_None
        ITIScodes_Construction = ["7941", "7443"]                                       # in-road-construction-area reduce-your-speed
        ITIScodes_Congestion = ["263", "7201"]                                          # traffic-congestion be-prepared-to-stop                    

        jsonRsa = {
            "MessageFrame":{
                "messageId":"27",
                "value":{
                    "RoadSideAlert":{
                        "msgCnt":"0",
                        "timeStamp":"0",
                        "typeEvent":261,
                        "description":{
                            "ITIScodes": []
                        }
                    }
                }
            } 
        }

        ItisTypes = self.ItisTypes

        if (itis_type == ItisTypes.type_explosion):
            itis_codes_to_send = ITIScodes_Explosion
        elif (itis_type == ItisTypes.type_accident):
            itis_codes_to_send = ITIScodes_Accident
        elif (itis_type == ItisTypes.type_fog):
            itis_codes_to_send = ITIScodes_Fog
        elif (itis_type == ItisTypes.type_congestion):
            itis_codes_to_send = ITIScodes_Congestion
        elif (itis_type == ItisTypes.type_construction):
            itis_codes_to_send = ITIScodes_Construction
        elif (itis_type == ItisTypes.type_violation):
            itis_codes_to_send = ITIScodes_Violation
        else:
            itis_codes_to_send = ITIScodes_None

        jsonRsa["MessageFrame"]["value"]["RoadSideAlert"]["description"]["ITIScodes"] = itis_codes_to_send  # change it to anything above for testing


        # var p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 int32 = 0,0,0,0,0,0,0,0,0,0,0,0
        p0, p1, p2, p3 = 0, 0, 0, 0
        
        lineId = rsa_id
        desc = rsa_desc
        p0 = rsa_pos['lat_start']
        p1 = rsa_pos['long_start']
        p2 = rsa_pos['lat_end']
        p3 = rsa_pos['long_end']
        endPoints = [p0, p1, p2, p3]
        return self.setRsaLine(lineId, endPoints, json.dumps(jsonRsa))
        
    def setRsaLine(self, lineId:str, endPoints, jsonRsa:str) -> bytes:

        now_time = datetime.now()
        # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
        msg_end_time = now_time + timedelta(minutes=1)
        
        # utc_now_time = now_time.replace(tzinfo=timezone.utc)
        # utc_msg_end_time = msg_end_time.replace(tzinfo=timezone.utc)
    
        seconds_now = int(now_time.timestamp())
        seconds_end = int(msg_end_time.timestamp())
        
        nanos_now = int(now_time.timestamp() % 1e9 )
        nanos_end = int(msg_end_time.timestamp() % 1e9)
        
        print("Original")
        print(f"Full: {now_time} Seconds: {seconds_now} Nano: {int()}")
     #   print(f"Full: {msg_end_time} Seconds: {seconds_end} Nano: {msg_end_time.strftime(('%s'))}")
        
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
