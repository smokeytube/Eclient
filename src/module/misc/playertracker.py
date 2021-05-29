# /py src/module/misc/playertracker

from mine import *
import time
import math
from src.module.functions import loadconfig

def Main():
    mc = Minecraft()
    modulenm = "PlayerTracker"
    configs = loadconfig()['modules'][modulenm]
    TrackerFreq = configs['playertrackerfreq']
    whichEntity = 0
    while True:
        entitys = mc.getPlayerEntityIds()
        player = mc.getPlayerId()

        posplayer = mc.entity.getPos(player)
        distances = {}
        for entit in entitys:
            try:
                posentity = mc.entity.getPos(entit)
            except:
                continue
            diffx = posentity.x - posplayer.x
            diffz = posentity.z - posplayer.z
            diffy = posentity.y - posplayer.y
            distance = math.sqrt((diffx ** 2) + (diffy ** 2) + (diffz ** 2))
            if distance == 0.0:
                continue
            distances[entit] = distance
        

        try:
            lowestdistuple = min(distances.items(), key=lambda x: x[1])
            lowestdistanceguy, dista = lowestdistuple
        except:
            continue

        if player == lowestdistanceguy:
            continue


        try:
            posentity = mc.entity.getPos(lowestdistanceguy)
        except:
            posentity = mc.entity.getPos(entitys[0])

        diffx = posentity.x - posplayer.x
        diffy = posentity.y - posplayer.y
        diffz = posentity.z - posplayer.z

        try:
            chatmsg = (mc.entity.getName(lowestdistanceguy))
        except:
            chatmsg = (mc.entity.getName(entitys[0]))
        mc.postToChat(chatmsg)

        distance = math.sqrt((diffx ** 2) + (diffy ** 2) + (diffz ** 2))
        mc.postToChat(distance)

        time.sleep(TrackerFreq)

if __name__ == '__main__':
    Main()