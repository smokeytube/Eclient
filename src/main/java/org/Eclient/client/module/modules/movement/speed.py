#// /py src/main/java/org/Eclient/client/module/modules/movement/speed
import input as input;
from mine import *;
from mcpi.minecraft import *;
import json;
import os;



class Speed:
    @staticmethod
    def loadconfig() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main() -> None:
        mc: object = Minecraft();
        modulenm: str = str(__class__.__name__);
        configs: list = Speed.loadconfig()['modules'][modulenm];
        player: int = mc.getPlayerId();
        moveamount: float = configs['travelspeed'];

        while True:
            pos: object = mc.entity.getPos(player);
            yaw: object = mc.entity.getRotation(player);
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