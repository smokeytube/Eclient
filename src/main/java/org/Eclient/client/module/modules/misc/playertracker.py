#//This module isn't finished yet. Please check later
#// /py src/main/java/org/Eclient/client/module/modules/misc/playertracker

from mine import *;
import time;
import json;
import math;
import os;


class PlayerTracker:
    def loadconfig():
        with open(os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\Eclientconfig.json') as configpath:
            return json.load(configpath);

    def Main():
        mc = Minecraft();
        modulenm = str(__class__.__name__);
        configs = PlayerTracker.loadconfig()['modules'][modulenm];
        TrackerFreq = configs['playertrackerfreq'];
        whichEntity = 0;
        while True:
            entitys = mc.getPlayerEntityIds();
            player = mc.getPlayerId();
            try:
                posentity = mc.entity.getPos(entitys[whichEntity]);
            except:
                posentity = mc.entity.getPos(entitys[0]);
            posplayer = mc.entity.getPos(player);
            diffx = posentity.x - posplayer.x;
            diffy = posentity.y - posplayer.y;
            diffz = posentity.z - posplayer.z;

            try:
                chatmsg = (mc.entity.getName(entitys[whichEntity]));
            except:
                chatmsg = (mc.entity.getName(entitys[0]));
            mc.postToChat(chatmsg);

            distance = math.sqrt((diffx ** 2) + (diffy ** 2) + (diffz ** 2));
            mc.postToChat(distance);

            if distance == 0.0:
                whichEntity += 1;

            time.sleep(TrackerFreq);

if __name__ == '__main__':
    PlayerTracker.Main();