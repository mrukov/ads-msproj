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
food= 0

SLEEP = 10

def incrementIndex(state):
    global rain
    global hot
    global cold
    global food
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
    if state == "food":
        food = food + 1
        if food == length:
            food = 0
    
    #print len(countFiles)

def getState():

    hour = datetime.datetime.now().hour
    if hour >= 14 and hour <= 12:
        return "food"

     # if not during lunchtime, get weather status
    key = "beee2caedc09e8322992562b541729d3"
    URL = "http://api.openweathermap.org/data/2.5/forecast?id=" + tm + "&units=metric&APPID=" + key
    response = requests.get(URL)
    formatted_response = response.json()
    
    if '3h' in formatted_response['list'][0]['rain']:
        return "rain"
    elif formatted_response['list'][0]['main']['temp'] > 25:
        return "hot"
    elif formatted_response['list'][0]['main']['temp'] < 5:
        return "cold"
    else:
        return "default"


def getPicture(s):
    scriptName = 'sh ./ms-script.sh'
    picture = "../ads/"+s
    sleep = str(SLEEP)
    resolution = "1920x1080"
    if s == "rain":
        state = rain
    if s == "hot":
        state = hot
    if s == "cold":
        state = cold
    if s == "food":
        state = food
    if s == "default":
        state = 0
    incrementIndex(s)
    params = scriptName + " " + picture + " " + sleep + " " + resolution + " " + str(state)
    os.system(params)
 


for i in range(0, 10):
    st = getState()
    getPicture(st)
