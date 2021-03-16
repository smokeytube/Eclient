#// /py src/main/java/org/Eclient/client/module/modules/movement/gocrazy.py

import input as input;
from mine import *;
from mcpi.minecraft import *;
import json;
import os;
import random;



class GoCrazy:
    @staticmethod
    def loadconfig() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    @staticmethod
    def Main() -> None:
        mc: object = Minecraft();
        modulenm: str = str(__class__.__name__);
        configs: list = GoCrazy.loadconfig()['modules'][modulenm];
        player: int = mc.getPlayerId();
        crazyamount: float = configs['crazyamount'];
        if crazyamount < 1:
            crazyamount: int = int(crazyamount*10);
            under1: bool = True;
        else:
            crazyamount: int = int(crazyamount)
            under1: bool = False;

        def gostupid() -> float:
            if under1:
                return ((random.randint(1, crazyamount))/10);
            else:
                return random.randint(1, crazyamount);

        while True:
            pos: object = mc.entity.getPos(player);
            yaw: float = mc.entity.getRotation(player);
            move: bool = False;

            if input.wasPressedSinceLast(input.KEY_W):
                pos.z -= gostupid() * sin(radians(yaw));
                pos.x -= gostupid() * cos(radians(yaw));
                pos.z += gostupid() * sin(radians(yaw));
                pos.x += gostupid() * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.KEY_S):
                pos.z += gostupid() * sin(radians(yaw));
                pos.x += gostupid() * cos(radians(yaw));
                pos.z -= gostupid() * sin(radians(yaw));
                pos.x -= gostupid() * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.KEY_D):
                pos.x += gostupid() * -sin(radians(yaw));
                pos.z += gostupid() * cos(radians(yaw));
                pos.x -= gostupid() * -sin(radians(yaw));
                pos.z -= gostupid() * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.KEY_A):
                pos.x -= gostupid() * -sin(radians(yaw));
                pos.z -= gostupid() * cos(radians(yaw));
                pos.x += gostupid() * -sin(radians(yaw));
                pos.z += gostupid() * cos(radians(yaw));
                move: bool = True;
            if input.wasPressedSinceLast(input.SPACE):
                posorneg: int = random.randint(1,2);
                if posorneg == 1:
                    pos.y += gostupid();
                else:
                    pos.y -= gostupid();
                move: bool = True;
            if move:
                try:
                    mc.entity.setPos(player,pos);
                except:
                    mc.postToChat("Error with "+modulenm);


if __name__ == '__main__':
    GoCrazy.Main();