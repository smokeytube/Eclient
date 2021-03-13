#// /py src/main/java/org/Eclient/client/module/modules/movement/phase
import input as input;
from mine import *;
from mcpi.minecraft import *;
import json;
import os;
import time;

    

class Phase:
    @staticmethod
    def loadconfig() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);
        
    def Main() -> None:
        mc: object = Minecraft();
        modulenm: str = str(__class__.__name__);
        configs: list = Phase.loadconfig()['modules'][modulenm];
        player: int = mc.getPlayerId();
        Yspeed: float = configs['phaseamount'];

        while True:
            pos: object = mc.entity.getPos(player);
            move: bool = False;
            if input.wasPressedSinceLast(input.KEY_PLUS):
                pos.y += Yspeed;
                move: bool = True;
            if input.wasPressedSinceLast(input.KEY_MINUS):
                pos.y -= Yspeed;
                move: bool = True;
            if move:
                try:
                    mc.entity.setPos(player,pos);
                except:
                    mc.postToChat("Error");

if __name__ == '__main__':
    Phase.Main();
    