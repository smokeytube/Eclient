#// /py src/main/java/org/Eclient/client/module/modules/misc/playertracker.py

from typing import Any;
from mine import *;
import time;
import json;
import math;
import os;


class PlayerTracker:
    @staticmethod
    def loadconfig() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main() -> None:
        mc: object = Minecraft();
        modulenm: str = str(__class__.__name__);
        configs: dict = PlayerTracker.loadconfig()['modules'][modulenm];
        TrackerFreq: int = configs['playertrackerfreq'];
        whichEntity: int = 0;
        while True:
            entitys: list = mc.getPlayerEntityIds();
            player: int = mc.getPlayerId();
            try:
                posentity: object = mc.entity.getPos(entitys[whichEntity]);
            except:
                posentity: object = mc.entity.getPos(entitys[0]);

            posplayer: object = mc.entity.getPos(player);
            diffx: float = posentity.x - posplayer.x;
            diffy: float = posentity.y - posplayer.y;
            diffz: float = posentity.z - posplayer.z;

            try:
                chatmsg: str = (mc.entity.getName(entitys[whichEntity]));
            except:
                chatmsg: str = (mc.entity.getName(entitys[0]));
            mc.postToChat(chatmsg);

            distance: float = math.sqrt((diffx ** 2) + (diffy ** 2) + (diffz ** 2));
            mc.postToChat(distance);

            if distance == 0.0:
                whichEntity += 1;

            time.sleep(TrackerFreq);

if __name__ == '__main__':
    PlayerTracker.Main();