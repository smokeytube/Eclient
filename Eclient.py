#// /py Eclient

#// This is the main file

#// External libs
import json
from multiprocessing import Process
import os

#// GUI
# from src.main.java.org.Eclient.client.gui.EclientGUI import EclientGUI as eclientgui

#// Movement
from src.module.movement.speed import Main as speed
from src.module.movement.phase import Main as phase
from src.module.movement.gocrazy import Main as gocrazy
from src.module.movement.autosprint import Main as autosprint

#// Statistical
from src.module.statistical.movementlogger import Main as movementlogger
from src.module.statistical.keymapper import Main as keymapper

#// Chat
from src.module.chat.chatlogger import Main as chatlogger

#// Misc
from src.module.misc.playertracker import Main as playertracker



class Eclient:
    @staticmethod
    def loadjson():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\Eclientconfig.json') as configpath:
            return json.load(configpath)

    @staticmethod
    def Main():
        #// Initaite GUI
        #Process(target=eclientgui.Main).start()

        #// Movement
        configs = Eclient.loadjson()['modules']

        if configs['Speed']['Enabled'] == True:
            Process(target=speed).start()

        if configs['Phase']['Enabled'] == True:
            Process(target=phase).start()

        if configs['GoCrazy']['Enabled'] == True:
            Process(target=gocrazy).start()

        if configs['AutoSprint']['Enabled'] == True:
            Process(target=autosprint).start()

        #// Statistical
        if configs['MovementLogger']['Enabled'] == True:
            Process(target=movementlogger).start()

        if configs['KeyMapper']['Enabled'] == True:
            Process(target=keymapper).start()

        #//Chat
        if configs['ChatLogger']['Enabled'] == True:
            Process(target=chatlogger).start()

        #// Misc
        if configs['PlayerTracker']['Enabled'] == True:
            Process(target=playertracker).start()


if __name__ == '__main__':
    Eclient.Main()
