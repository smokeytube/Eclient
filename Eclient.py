#// /py Eclient

#// This is the main file

#// External libs
import json;
import threading as Thread;
import os;

#// Movement
from src.main.java.org.Eclient.client.module.modules.movement.speed import Speed as speed;
from src.main.java.org.Eclient.client.module.modules.movement.phase import Phase as phase;

#// Statistical
from src.main.java.org.Eclient.client.module.modules.statistical.movementlogger import MovementLogger as movementlogger;

#// Misc
from src.main.java.org.Eclient.client.module.modules.misc.playertracker import PlayerTracker as playertracker;



class Main:
    def loadjson():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main():
        #// Movement
        configs = Main.loadjson()['modules'];

        if configs['Speed']['Enabled'] == True:
            Thread(target = speed.Main).start();

        if configs['Phase']['Enabled'] == True:
            Thread(target = phase.Main).start();

        #// Statistical
        if configs['MovementLogger']['Enabled'] == True:
            Thread(target = movementlogger.Main).start();

        #// Misc
        if configs['PlayerTracker']['Enabled'] == True:
            Thread(target = playertracker.Main).start();


if __name__ == '__main__':
    Main.Main();
