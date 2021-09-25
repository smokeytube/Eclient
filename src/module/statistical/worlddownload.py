# /py src/module/statistical/worlddownload

from mine import *
import time
import os
from src.module.functions import loadconfig

def Main():
    mc = Minecraft()
    modulenm = "WorldDownload"
    #configs = loadconfig()['modules'][modulenm]

    logpth = (os.getcwd()+"\\src\\module\\statistical\\data\\worlddownload\\world.txt")
    movelog = open(logpth, 'w')
    movelogtimeout = 0
    player = mc.getPlayerId()
    
    posplayer = mc.entity.getPos(player)

    x = int(posplayer.x)
    y = int(posplayer.y)
    z = int(posplayer.z)

    print(x, y, z)

    xrange = 30
    yrange = 40
    zrange = 30

    for i in range(x-xrange,x+xrange):
        for ii in range(y-yrange,y+yrange):
            for iii in range(z-zrange,z+zrange):
                posplayer = mc.entity.getPos(player)

                if movelogtimeout == 50:
                    movelog.close()
                    movelogtimeout = 0
                    movelog = open(logpth, 'a+')

                block = mc.entity.getBlock(i, ii, iii)
                if block == 0:
                    pass
                else:
                    movelog.write('{}|{}|{}|{}\n'.format(i-x, ii-y, iii-z, block))
                print('{} {} {}:{}\n'.format(i, ii, iii, block))

                movelogtimeout += 1


if __name__ == '__main__':
    Main()