#//This module isn't finished yet. Please check later
#// /py src/main/java/org/Eclient/client/module/modules/statistical/movementlogger.py

from mine import *;
import time;
import json;
import math;
import os;


class MovementLogger:
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main():
        mc = Minecraft();
        modulenm = str(__class__.__name__);
        configs = MovementLogger.loadconfig()['modules'][modulenm];
        LoggerFreq = configs['LoggingFreq'];

        movelog = open(os.getenv('Appdata')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\movementlogger\\movementlogger.txt', 'w');
        movelogtimeout = 0;
        player = mc.getPlayerId();
        
        while True:
            posplayer = mc.entity.getPos(player);
            x = posplayer.x;
            y = posplayer.y;
            z = posplayer.z;

            if movelogtimeout == 50:
                movelog.close();
                movelogtimeout = 0;
                movelog = open(os.getenv('Appdata')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\movementlogger\\movementlogger.txt', 'a+');

            movelog.write('{} {} {}\n'.format(x, y, z));

            movelogtimeout += 1;

            time.sleep(LoggerFreq);

if __name__ == '__main__':
    MovementLogger.Main();