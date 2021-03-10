#//This module isn't finished yet. Please check later
#// /py src/main/java/org/Eclient/client/module/modules/statistical/keymapper.py

from mine import *;
import time;
import json;
import math;
import os;


class KeyMapper:
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main():
        mc = Minecraft();
        modulenm = str(__class__.__name__);
        configs = KeyMapper.loadconfig()['modules'][modulenm];
        sleeptime = configs['sleep'];
        outputtxt = configs['outputfile'];

        keymapperpath = (os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\keymapper\\');
        os.system(keymapperpath+'keymapper.exe '+sleeptime+' '+keymapperpath+outputtxt);

if __name__ == '__main__':
    KeyMapper.Main();