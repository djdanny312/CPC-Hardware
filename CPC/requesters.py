import requests


def getParkCount():
    
    r = requests.get("https://cpc-uprm.azurewebsites.net/cpc/parkings/counter/1")
    print(r.status_code)
    
def pushParkCount(count):
    
    r = requests.post('https//cpc-uprm.azurewebsites.net/cpc/parkings/counter/1', data = {'occupancy':count})
    print(r.url)
    
def updateMaxCount():
    pass


if __name__=="__main__":
    count=5
    content = getParkCount()
    print(content)
    
    