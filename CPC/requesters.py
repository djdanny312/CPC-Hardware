import requests
import json
from variables import parking_id, admin_user, admin_pass,base_url

def getParkCount():
    #gets the Parking count that is currently on the server
    
    r = requests.get(base_url+"/parkings/counter/"+parking_id)
    return r.json()["occupancy"]

#pushes current parking count to the server
def pushParkCount(count):
    #sets a payload dictionary as a json
    payload = json.dumps({
        "email_address":admin_user,
        "password": admin_pass
        })
    headers={
        "Content-Type":"application/json"
        }
    #post a request to sign in as an admin and, return the token and account id
    r = requests.post(base_url+"/authenticate", headers=headers, data = payload)
    response = r.json()
    print(response)
    #a request to get the current parking, used to see the previous count before the update(for testing purposes)
    r = requests.get(base_url+"/parkings/counter/"+parking_id)
    print(r.json())
    
    payload = json.dumps({
        "account_id": response["account_id"],
        "token" : response["token"],
        "occupancy" : count
        })
    #puts the count stored in the mpu and pushed each time the enter or exit of vehicle is triggered
    r = requests.put(base_url+"/parkings/counter/"+parking_id,headers=headers, data = payload)
    print(r.json())
    return r.json()

#gets the parking password by id using requests  
def getParkPass():
    #sets a payload dictionary as a json
    payload = json.dumps({
        "email_address":admin_user,
        "password":admin_pass
        })
    headers={
        "Content-Type":"application/json"
        }
    #post a request to sign in as an admin and, return the token and account id
    r = requests.post(base_url+"/authenticate", headers = headers, data = payload)
    response = r.json()
    print(response)

    payload =({
        "account_id": response["account_id"],
        "token": response["token"]
        })
    #request to get the password, which is to be used as the salt for the hash function. For the specified parkinn_id
    r = requests.get(base_url+"/parkings/password/"+parking_id ,headers = headers, params = payload)
    password = r.json()["password"]
    
    print(password)
    return password
#gets all info from the parking depending on the parking id
def getParkInfo():
    r = requests.get(base_url+"/parkings/counter/"+parking_id)
    print(r.json())
    return r.json()