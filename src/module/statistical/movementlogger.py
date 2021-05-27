# /py src/module/statistical/movementlogger

from mine import *
import time
import os
from src.module.functions import loadconfig

def Main():
    mc = Minecraft()
    modulenm = "MovementLogger"
    configs = loadconfig()['modules'][modulenm]
    LoggerFreq = configs['loggingfreq']

    logpth = (os.getcwd()+"\\src\\module\\statistical\\data\\movementlogger\\movementlogger.txt")
    movelog = open(logpth, 'w')
    movelogtimeout = 0
    player = mc.getPlayerId()
    
    while True:
        posplayer = mc.entity.getPos(player)
        x = posplayer.x
        y = posplayer.y
        z = posplayer.z

        if movelogtimeout == 50:
            movelog.close()
            movelogtimeout = 0
            movelog = open(logpth, 'a+')

        movelog.write('{} {} {}\n'.format(x, y, z))

        movelogtimeout += 1

        time.sleep(LoggerFreq)


if __name__ == '__main__':
    Main()