# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64

URL = "http://openapi.xfyun.cn/v2/aiui"
APPID = "5ae9b166"
API_KEY = "e397d6acc6004afea833fc407fed2ed2"
AUE = "raw"
AUTH_ID = "2894c985bf8b1111c6728db79d3479ae"
DATA_TYPE = "audio"
SAMPLE_RATE = "16000"
SCENE = "main"
RESULT_LEVEL = "complete"
LAT = "39.938838"
LNG = "116.368624"
FILE_PATH = "output.wav"


def buildHeader():
    curTime = str(int(time.time()))
    param = "{\"result_level\":\""+RESULT_LEVEL+"\",\"auth_id\":\""+AUTH_ID+"\",\"data_type\":\""+DATA_TYPE+"\",\"sample_rate\":\""+SAMPLE_RATE+"\",\"scene\":\""+SCENE+"\",\"lat\":\""+LAT+"\",\"lng\":\""+LNG+"\"}"
    paramBase64 = base64.b64encode(param)

    m2 = hashlib.md5()
    m2.update(API_KEY + curTime + paramBase64)
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
    }
    return header


def readFile(filePath):
    binfile = open(filePath, 'rb')
    data = binfile.read()
    return data


def aiui():
    r = requests.post(URL, headers=buildHeader(), data=readFile(FILE_PATH))
    return r.content


if __name__ == "__main__":
    r = requests.post(URL, headers=buildHeader(), data=readFile(FILE_PATH))
    print(r.content)