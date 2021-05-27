#// /py src/main/java/org/Eclient/client/module/modules/movement/speed

import input as input;
from mine import *;
from mcpi.minecraft import *;
import json;
import os;



class Speed:
    @staticmethod
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    @staticmethod
    def Main():
        mc = Minecraft();
        modulenm = str(__class__.__name__);
        configs = Speed.loadconfig()['modules'][modulenm];
        player = mc.getPlayerId();
        moveamount = configs['travelspeed'];

        while True:
            pos = mc.entity.getPos(player);
            yaw = mc.entity.getRotation(player);
            move: bool = False;
            if input.wasPressedSinceLast(input.UP):
                pos.x += moveamount * -sin(radians(yaw));
                pos.z += moveamount * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.DOWN):
                pos.x -= moveamount * -sin(radians(yaw));
                pos.z -= moveamount * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.RIGHT):
                pos.z -= moveamount * sin(radians(yaw));
                pos.x -= moveamount * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.LEFT):
                pos.z += moveamount * sin(radians(yaw));
                pos.x += moveamount * cos(radians(yaw));
                move: bool = True;
            if move:
                try:
                    mc.entity.setPos(player,pos);
                except:
                    mc.postToChat("Error with "+modulenm);


if __name__ == '__main__':
    Speed.Main();