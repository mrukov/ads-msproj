import requests
import json
import time
import subprocess
import os
import datetime
import sys
from subprocess import call
from pprint import pprint

tm = "665087"
bangkok=  "1609350"

rain = 0
hot = 0
cold = 0
lunch = 0

SLEEP = 5

def incrementIndex(state):
    global rain
    global hot
    global cold
    global lunch
    dir = "../ads/" + state
    countFiles = next(os.walk(dir))[2] 
    length = len(countFiles)
    if state == "rain":
        rain = rain + 1
        if rain == length:
            rain = 0
    if state == "hot":
        hot = hot + 1
        if hot == hot:
            hot = 0
    if state == "cold":
        cold = cold + 1
        if cold == length:
            cold = 0
    if state == "lunch":
        lunch = lunch + 1
        if lunch == length:
            lunch = 0
    
    #print len(countFiles)

def getState():

    hour = datetime.datetime.now().hour
    if hour >= 11 and hour <= 12:
        return "lunch"

     # if not during lunchtime, get weather status
    key = "beee2caedc09e8322992562b541729d3"
    URL = "http://api.openweathermap.org/data/2.5/forecast?id=" + tm + "&units=metric&APPID=" + key
    response = requests.get(URL)
    formatted_response = response.json()
    
    if '3h' in formatted_response['list'][0]['rain']:
        return "rain"
    elif formatted_response['list'][0]['main']['temp'] > 25:
        return "sunny"
    elif formatted_response['list'][0]['main']['temp'] < 5:
        return "cold"
    else:
        return "default"


def getPicture(s):
    scriptName = './ms-script.sh'
    picture = "../ads/"+s+".jpg"
    sleep = str(SLEEP)
    resolution = "1920x1080"
    params = scriptName + " " + picture + " " + sleep + " " + resolution
    os.system(params)
    

#state = getState()
#getPicture(state)
#getPicture("sunny")
#time.sleep(SLEEP-1)
#getPicture("rain")
#time.sleep(SLEEP-1)
#getPicture("default")
#time.sleep(SLEEP)
#time.sleep(10)

incrementIndex("food")
