#// /py src/main/java/org/Eclient/client/module/modules/movement/phase
import input as input;
from mine import *;
from mcpi.minecraft import *;
import json;
import os;
import time;

    

class Phase:
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);
        
    def Main():
        mc = Minecraft();
        modulenm = str(__class__.__name__);
        configs = Phase.loadconfig()['modules'][modulenm];
        player = mc.getPlayerId();
        Yspeed = configs['phaseamount'];

        while True:
            pos = mc.entity.getPos(player);
            move = False;
            if input.wasPressedSinceLast(input.KEY_PLUS):
                pos.y += Yspeed;
                move = True;
            if input.wasPressedSinceLast(input.KEY_MINUS):
                pos.y -= Yspeed;
                move = True;
            if move:
                try:
                    mc.entity.setPos(player,pos);
                except:
                    mc.postToChat("Error");

if __name__ == '__main__':
    Phase.Main();
    