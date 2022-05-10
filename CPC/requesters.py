import requests
import json

base_url= "https://cpc-uprm.azurewebsites.net/cpc"


def getParkCount():
    
    r = requests.get(base_url+"/parkings/counter/18")
    print(r.status_code)
    return r.json()["occupancy"]

def pushParkCount(count):
    payload = json.dumps({
        "email_address":"hector.rivera84@upr.edu",
        "password": "12345678"
        })
    headers={
        "Content-Type":"application/json"
        }
    r = requests.post(base_url+"/authenticate", headers=headers, data = payload)
    response = r.json()
    print(response)
    r = requests.get(base_url+"/parkings/counter/18")
    print(r.json())
    
    payload = json.dumps({
        "account_id": response["account_id"],
        "token" : response["token"],
        "occupancy" : count
        })
    
    r = requests.put(base_url+"/parkings/counter/5",headers=headers, data = payload)
    print(r.json())
    return r.json()
    

def getParkInfo():
    
    r = requests.get(base_url+"/parkings/counter/18")
    print(r.status_code)
    return r.json()

if __name__=="__main__":
    pushParkCount(5)
    pushParkCount(0)
    
    
    