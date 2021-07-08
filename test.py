# -*- coding: utf8 -*-
import requests
from requests import Session
from time import sleep

def send(message):
    api = "https://sctapi.ftqq.com/SCT35322TXSHWtkwibbhznT5DWWGq7SrR.send"
    title = u"百度贴吧签到"
    data = {
        "text": title,
        "desp": message
    }
    req = requests.post(api, data=data)
    
message = f'''测试Actions'''
print(message)
send(message)
