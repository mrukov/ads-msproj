import requests
import json
import time
import subprocess
import shlex
import os
import sys
from subprocess import call
from pprint import pprint

tm = "665087"
bangkok=  "1609350"

SLEEP = 5

def getState():
    API_KEY = "beee2caedc09e8322992562b541729d3"
    URL = "http://api.openweathermap.org/data/2.5/forecast?id=" + tm + "&units=metric&APPID=" + API_KEY
    response = requests.get(URL)
    formatted_response = response.json()

    if '3h' in formatted_response['list'][0]['rain']:
        return "Rain"
    elif formatted_response['list'][0]['main']['temp'] > 25:
        return "Sunny"
    else:
        return "Default"
#    print formatted_response['list'][0]['rain']['3h']


def getPicture(s):
    scriptName = './ms-script.sh'
    picture = "../ads/"+s+".jpg"
    sleep = str(SLEEP)
    resolution = "1920x1080"
    params = scriptName + " " + picture + " " + sleep + " " + resolution
    #subprocess.call(params)
    os.system(params)
    

#state = getState()
#getPicture(state)
getPicture("sunny")
time.sleep(SLEEP-1)
getPicture("rain")
time.sleep(SLEEP-1)
getPicture("default")
time.sleep(SLEEP)
#time.sleep(10)
