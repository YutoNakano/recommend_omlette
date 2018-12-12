#coding: UTF-8
import Scraping
import json


def writeData(list_data):
    fw = open("main.json", 'w')
    json.dump(list_data, fw)
    fw.close()
    jsonDict = open("main.json", "r")
    return json.load(jsonDict)


def dic(rist_result):
    for i in rist_result:
        return i
