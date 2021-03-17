#// /py Eclient

#// This is the main file

#// External libs
import json;
from multiprocessing import Process;
import os;

#// GUI
from src.main.java.org.Eclient.client.gui.EclientGUI import EclientGUI as eclientgui;

#// Movement
from src.main.java.org.Eclient.client.module.modules.movement.speed import Speed as speed;
from src.main.java.org.Eclient.client.module.modules.movement.phase import Phase as phase;
from src.main.java.org.Eclient.client.module.modules.movement.gocrazy import GoCrazy as gocrazy;
from src.main.java.org.Eclient.client.module.modules.movement.autosprint import AutoSprint as autosprint;

#// Statistical
from src.main.java.org.Eclient.client.module.modules.statistical.movementlogger import MovementLogger as movementlogger;
from src.main.java.org.Eclient.client.module.modules.statistical.keymapper import KeyMapper as keymapper;

#// Chat
from src.main.java.org.Eclient.client.module.modules.chat.chatlogger import ChatLogger as chatlogger;

#// Misc
from src.main.java.org.Eclient.client.module.modules.misc.playertracker import PlayerTracker as playertracker;



class Main:
    @staticmethod
    def loadjson() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    @staticmethod
    def Main() -> None:
        #// Initaite GUI
        Process(target=eclientgui.Main).start();

        #// Movement
        configs: dict = Main.loadjson()['modules'];

        if configs['Speed']['Enabled'] == True:
            Process(target=speed.Main).start();

        if configs['Phase']['Enabled'] == True:
            Process(target=phase.Main).start();

        if configs['GoCrazy']['Enabled'] == True:
            Process(target=gocrazy.Main).start();

        if configs['AutoSprint']['Enabled'] == True:
            Process(target=autosprint.Main).start();

        #// Statistical
        if configs['MovementLogger']['Enabled'] == True:
            Process(target=movementlogger.Main).start();

        if configs['KeyMapper']['Enabled'] == True:
            Process(target=keymapper.Main).start();

        #//Chat
        if configs['ChatLogger']['Enabled'] == True:
            Process(target=chatlogger.Main).start();

        #// Misc
        if configs['PlayerTracker']['Enabled'] == True:
            Process(target=playertracker.Main).start();


if __name__ == '__main__':
    Main.Main();
