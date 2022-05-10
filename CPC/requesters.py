import requests
import json

base_url= "https://cpc-uprm.azurewebsites.net/cpc"

def getParkCount():
    #gets the Parking count that is currently on the server
    r = requests.get(base_url+"/parkings/counter/18")
    print(r.status_code)
    return r.json()["occupancy"]

#pushes current parking count to the server
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
    
    r = requests.put(base_url+"/parkings/counter/18",headers=headers, data = payload)
    print(r.json())
    return r.json()

#gets the parking password by id using requests  
def getParkPass(park_num):
    
    num = str(park_num)
    payload = json.dumps({
        "email_address":"hector.rivera84@upr.edu",
        "password": "12345678"
        })
    headers={
        "Content-Type":"application/json"
        }
    r = requests.post(base_url+"/authenticate", headers = headers, data = payload)
    response = r.json()
    print(response)

    payload = json.dumps({
        "account_id": response["account_id"],
        "token": response["token"]
        }) 
    r = requests.get(base_url+"/parkings/password/"+num ,headers = headers, params = payload)
    password = r.json()
    
    print(password)
    return password
#gets all info from the parking depending on the parking id
def getParkInfo(park_num):
    
    parking = str(park_num)
    r = requests.get(base_url+"/parkings/counter/"+parking)
    print(r.status_code)
    return r.json()

if __name__=="__main__":
    getParkPass(18)
    
    
    