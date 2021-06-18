# /py src/module/misc/playertracker

from mine import *
import time
import math
import win32api, win32con
from src.module.functions import loadconfig
import keyboard

def Main():
    mc = Minecraft()
    modulenm = "Killaura"
    configs = loadconfig()['modules'][modulenm]
    cps = 1/int(configs['cps'])
    mode = configs['mode']
    whichEntity = 0
    while True:
        if keyboard.is_pressed('r'):
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
            diffz = posentity.z - posplayer.z
            diffy = posentity.y - posplayer.y
            newpitch = 0
            newyaw = 0
            distance = math.sqrt((diffx ** 2) + (diffy ** 2) + (diffz ** 2))

            try:
                newpitch = math.degrees(-math.tan(diffy/distance))
                newyaw = math.degrees(math.atan2(diffz, diffx))
            except:
                mc.postToChat("epic fail")

            distance = math.sqrt((diffx ** 2) + (diffy ** 2) + (diffz ** 2))

            if distance == 0.0:
                whichEntity += 1
            elif distance > 0.2 and distance < 4:
                mc.entity.setRotation(player, newyaw-90)
                mc.entity.setPitch(player, newpitch)
                if mode == 'pre':
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            
            time.sleep(cps)


if __name__ == '__main__':
    Main()