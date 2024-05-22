import requests
import json

def register_client():
    
    crs_url = "http://vzmode.las.wl.dltdemo.io:30413/registration"
    client_data = { "ClientInformation":{ "EntityType":"VEH", "EntitySubtype":"PSGR", "VendorID":"MCAS" }, "BSM":{ "MsgFormat":"UPER" }, "RSA":{ "MsgFormat":"UPER" }, "PSM":{ "MsgFormat":"UPER" }, "MAP":{ "MsgFormat":"UPER" }, "SPAT":{ "MsgFormat":"UPER" } }
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(crs_url, data=json.dumps(client_data), headers=headers)

    js = json.loads(r.text)
    reg_id = js.get('ID')
    print(reg_id)
  
def main():
    register_client()

    
if __name__ == "__main__":
    main()
   