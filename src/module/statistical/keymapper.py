# /py src/module/statistical/keymapper

from mine import *
import os
from src.module.functions import loadconfig

def Main():
    modulenm = "KeyMapper"
    configs = loadconfig()['modules'][modulenm]
    sleeptime = configs['sleep']
    outputtxt = configs['outputfile']

    keymapperpath = (os.getcwd()+"\\src\\module\\statistical\\data\\keymapper\\")
    os.system(keymapperpath+'keymapper.exe '+str(sleeptime)+' '+keymapperpath+outputtxt)


if __name__ == '__main__':
    Main()