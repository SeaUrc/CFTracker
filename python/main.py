import requests
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import numpy as np


def req(activeOnly=False, includeRetired=False):
    url = f'https://codeforces.com/api/user.ratedList?activeOnly={activeOnly}&includeRetired={includeRetired}'
    res = requests.get(url=url)
    return res.json()

def display_limited_json_structure(json_obj, max_depth=3, max_items=100):
    def limit_json(obj, depth):
        if depth > max_depth:
            return "..."
        if isinstance(obj, dict):
            return {k: limit_json(v, depth + 1) for k, v in list(obj.items())[:max_items]}
        elif isinstance(obj, list):
            return [limit_json(i, depth + 1) for i in obj[:max_items]]
        return obj

    limited_json = limit_json(json_obj, 0)
    formatted_json = json.dumps(limited_json, indent=2, sort_keys=True)
    print(formatted_json)

# display_limited_json_structure(res)
def generateRanking():
    res = req()
    ranking = np.empty((len(res["result"]), 2), dtype=np.int32)

    i = 0
    for user in res["result"]:
        try:
            ranking[i][0] = user['rating']
            ranking[i][1] = 1 # get problems solved all time here
        except:
            print(user)
            break
        i+=1
    

PATH = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome()

def getProfile(user):
    driver.get("https://codeforces.com/profile/" + user)

def getProblemsSolvedAllTime():
    return driver.find_elements(By.CLASS_NAME, '_UserActivityFrame_counterValue')[0]

getProfile("SeaUrc")
print(getProblemsSolvedAllTime())