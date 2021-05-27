import json
import os

def loadconfig():
    with open(os.getcwd()+'\\src\\Eclientconfig.json') as configpath:
        return json.load(configpath)