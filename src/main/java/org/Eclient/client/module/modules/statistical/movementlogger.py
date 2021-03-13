#//This module isn't finished yet. Please check later
#// /py src/main/java/org/Eclient/client/module/modules/statistical/movementlogger.py

from io import TextIOWrapper
from typing import TextIO
from mine import *;
import time;
import json;
import os;


class MovementLogger:
    @staticmethod
    def loadconfig() -> dict:
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main() -> None:
        mc: object = Minecraft();
        modulenm: str = str(__class__.__name__);
        configs: list = MovementLogger.loadconfig()['modules'][modulenm];
        LoggerFreq: float = configs['loggingfreq'];

        movelog: TextIOWrapper = open(os.getenv('Appdata')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\movementlogger\\movementlogger.txt', 'w');
        movelogtimeout: int = 0;
        player: int = mc.getPlayerId();
        
        while True:
            posplayer: object = mc.entity.getPos(player);
            x: float = posplayer.x;
            y: float = posplayer.y;
            z: float = posplayer.z;

            if movelogtimeout == 50:
                movelog.close();
                movelogtimeout: int = 0;
                movelog: TextIOWrapper = open(os.getenv('Appdata')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\movementlogger\\movementlogger.txt', 'a+');

            movelog.write('{} {} {}\n'.format(x, y, z));

            movelogtimeout += 1;

            time.sleep(LoggerFreq);


if __name__ == '__main__':
    MovementLogger.Main();