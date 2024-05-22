import time
from datetime import datetime, timedelta, timezone

import imp_core.routed_msg_vzmode.routed_msg_pb2 as routed_msg_pb2
from google.protobuf import timestamp_pb2

class Rsa_Helper:
    def __init__(self):
        pass

    def get_rsa_message(self, rsa_id:str, rsa_desc:str, rsa_pos) -> bytes:
        #  I don't know the best location to store these as static strings in your Go project.
        #  I left them here for simplicity but they should probably be in a safer, more remote
        #  location, along with any other line crossing RSA messages that you want to send.

        #  ****** Reduced Speed Ahead Slow Down ******
        jsonRsa1 = '''
        {
            "MessageFrame":{
                "messageId":"27",
                "value":{
                    "RoadSideAlert":{
                        "msgCnt":"0",
                        "timeStamp":"0",
                        "typeEvent":261,
                        "description":{
                            "ITIScodes": ["12302", "268", "13569", "7201"]
                        }
                    }
                }
            } 
        }
        
        '''

        # Check document(J2540_2) page 215 for examples of proper encoding

        # ****** Slow Traffic Ahead Proceed With Caution ******
        # jsonRsa2 = 
        # {
        #     "MessageFrame":{
        #         "messageId":"27",
        #         "value":{
        #             "RoadSideAlert":{
        #                 "msgCnt":"0",
        #                 "timeStamp":"0",
        #                 "typeEvent":261,
        #                 "description":{
        #                     "ITIScodes": ["259", "13569", "7714", "12330"]
        #                 }
        #             }
        #         }
        #     }
        # }

        # ****** Delay 10 Minute Delay Interstate 10 Westbound Traffic ******
        # jsonRsa3 = 
        # {
        #     "MessageFrame":{
        #         "messageId":"27",
        #         "value":{
        #             "RoadSideAlert":{
        #                 "msgCnt":"0",
        #                 "timeStamp":"0",
        #                 "typeEvent":261,
        #                 "description":{
        #                     "ITIScodes": ["1537", "12554", "8728", "1537", "11781", "12554", "7997"]
        #                 }
        #             }
        #         }
        #     }
        # }


        # var p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 int32 = 0,0,0,0,0,0,0,0,0,0,0,0
        p0, p1, p2, p3 = 0, 0, 0, 0

        # lineId = "inrixIncidentID_1"
        # endPoints = [4]int32 {p0, p1, p2, p3}
        # setRsaLine (lineId, endPoints, jsonRsa1)

        # lineId = "inrixIncidentID_2"
        # endPoints = [4]int32 {p4, p5, p6, p7}
        # setRsaLine (lineId, endPoints, jsonRsa2)

        # lineId = "inrixIncidentID_3"
        # endPoints = [4]int32 {p8, p9, p10, p11}
        # setRsaLine (lineId, endPoints, jsonRsa3)

        # lineId = "Test_IncidentID_1"
        # p0 = 334800020
        # p1 = -1120383930
        # p2 = 334799823
        # p3 = -1120382324
        # endPoints := [4]int32 {p0, p1, p2, p3}
        # setRsaLine (lineId, endPoints, jsonRsa1)
        
        lineId = rsa_id
        desc = rsa_desc
        p0 = rsa_pos['lat_start']
        p1 = rsa_pos['long_start']
        p2 = rsa_pos['lat_end']
        p3 = rsa_pos['long_end']
        endPoints = [p0, p1, p2, p3]
        return self.setRsaLine(lineId, endPoints, jsonRsa1)
        
    def setRsaLine(self, lineId:str, endPoints, jsonRsa:str) -> bytes:

        now_time = datetime.now()
        # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) 
        msg_end_time = now_time + timedelta(minutes=2) 
        
        # utc_now_time = now_time.replace(tzinfo=timezone.utc)
        # utc_msg_end_time = msg_end_time.replace(tzinfo=timezone.utc)
    
        seconds_now = int(now_time.timestamp())
        seconds_end = int(msg_end_time.timestamp())
        
        nanos_now = int(now_time.timestamp() % 1e9 )
        nanos_end = int(msg_end_time.timestamp() % 1e9)
        
        print("Original")
        print(f"Full: {now_time} Seconds: {seconds_now} Nano: {int()}")
        print(f"Full: {msg_end_time} Seconds: {seconds_end} Nano: {msg_end_time.strftime(('%s'))}")
        
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
