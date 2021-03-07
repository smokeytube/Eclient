#// /py Eclient

#// This is the main file

#// External libs
import json;
from multiprocessing import Process;
import os;

#// Movement
from src.main.java.org.Eclient.client.module.modules.movement.speed import Speed as speed;
from src.main.java.org.Eclient.client.module.modules.movement.phase import Phase as phase;
from src.main.java.org.Eclient.client.module.modules.movement.gocrazy import GoCrazy as gocrazy;
from src.main.java.org.Eclient.client.module.modules.movement.autosprint import AutoSprint as autosprint;

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

        #// Misc
        if configs['PlayerTracker']['Enabled'] == True:
            Process(target=playertracker.Main).start();


if __name__ == '__main__':
    Main.Main();
