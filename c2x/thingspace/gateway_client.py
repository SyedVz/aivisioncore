import os
import requests


class GatewayClient:
    API_EVIDENCE = '{}/api/v1/accounts/{}/sources/{}/evidences/{}'
    API_INCIDENT = '{}/api/v1/incidents'

    KEY_ID = 'id'
    KEY_STATUS = 'status'
    KEY_MESSAGE = 'message'


    def __init__(self,
                 media_host=None,
                 media_port=None,
                 account_id=None,
                 source_id=None,
                 application_id=None,
                 ignore_errors=True):
        self.media_host = media_host
        self.media_port = media_port
        self.account_id = account_id
        self.source_id = source_id
        self.application_id = application_id
        self.ignore_errors = ignore_errors
        self.api_url = f'{self.media_host}:{self.media_port}'
        self.valid = False

        try:
            _ = requests.options(self.api_url)
            self.valid = True
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError) as e:
            print(f"GatewayClient Failure - Unable to establish connection: {e}.")
        except Exception as e:
            print(f"GatewayClient Failure - Unknown error occurred: {e}.")

        if self.valid:
            print(f'GatewayClient connecting to: {self.api_url}')
            self.api_evidence_img = GatewayClient.API_EVIDENCE.format(self.api_url, self.account_id, self.source_id, 'image')
            self.api_evidence_video = GatewayClient.API_EVIDENCE.format(self.api_url, self.account_id, self.source_id, 'video')
            self.api_evidence_bursts = GatewayClient.API_EVIDENCE.format(self.api_url, self.account_id, self.source_id, 'bursts')
            self.api_incident = GatewayClient.API_INCIDENT.format(self.api_url)


    def is_valid(self):
        return self.valid
    

    def get_media(self):
        return self.rtsp_url


    def __check_validity(self):
        if not self.is_valid():
            if self.ignore_errors:
                print('Uninitialized, cannot continue')
                return False
            else:
                raise RuntimeError('Uninitialized, cannot continue')
            
        return True
    

    def __post_and_get_json(self, url, json_data):
        try:
            response = requests.post(url, json=json_data)
            response.raise_for_status()
            rjson = response.json()
            return rjson
        except Exception as e:
            if self.ignore_errors:
                print(f'GatewayClient: Could not post: {e}')
                return None
            else:
                raise e
    

    def __create_incident(self, incident_type, description, evidences):
        if not self.__check_validity():
            return
        
        incident_data = {"applicationID": self.application_id, 
                         "type": incident_type,
                         "description": description,
                         "deploymentId": "22892a2d-7209-45f4-b09a-0a4e3ed0a698", # TODO: Get this from env?
                         "evidences": [{GatewayClient.KEY_ID: e for e in evidences}]}
        
        rjson = self.__post_and_get_json(self.api_incident, incident_data)
        if rjson is not None:
            if GatewayClient.KEY_ID not in rjson:
                print(f'GatewayClient: Error {rjson[GatewayClient.KEY_STATUS]}: {rjson[GatewayClient.KEY_MESSAGE]}')
                return None
            
            iid = rjson[GatewayClient.KEY_ID]
        else:
            return None
        
        return iid
    
    
    def __parse_evidence_json(self, rjson):
        if GatewayClient.KEY_ID not in rjson:
            print(f'GatewayClient: Could not parse evidence response: {rjson[GatewayClient.KEY_STATUS]}: {rjson[GatewayClient.KEY_MESSAGE]}')
            return None
        
        return rjson[GatewayClient.KEY_ID]


    def report_image(self, timestamp, report_type, description):
        # TODO: What is timestamp? How is it synced with Thingspace API?
        if not self.__check_validity():
            return
        
        evidence_data = {"frameTime": timestamp}
        rjson = self.__post_and_get_json(self.api_evidence_img, evidence_data)
        if rjson is not None:
            eid = self.__parse_evidence_json(rjson)
            if eid is not None:
                print(f'Created evidence: {eid}')
                iid = self.__create_incident(report_type, description, [eid])
                print(f'Created incident: {iid}')


    def report_video(self, time_start, time_stop, report_type, description):
        if not self.__check_validity():
            return
        
        evidence_data = {'startTime': time_start, 'endTime': time_stop}
        rjson = self.__post_and_get_json(self.api_evidence_video, evidence_data)
        if rjson is not None:
            eid = self.__parse_evidence_json(rjson)
            if eid is not None:
                print(f'Created evidence: {eid}')
                iid = self.__create_incident(report_type, description, [eid])
                print(f'Created incident: {iid}') 


    def report_bursts(self, time_start, time_stop, img_count, report_type, description):
        if not self.__check_validity():
            return
        
        evidence_data = {'startTime': time_start, 'endTime': time_stop, 'imageCount': img_count}
        rjson = self.__post_and_get_json(self.api_evidence_bursts, evidence_data)
        if rjson is not None:
            eid = self.__parse_evidence_json(rjson)
            if eid is not None:
                print(f'Created evidence: {eid}')
                iid = self.__create_incident(report_type, description, [eid])
                print(f'Created incident: {iid}')
        