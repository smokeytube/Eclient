# /py src/module/movement/gocrazy

import input as input
from mine import *
from mcpi.minecraft import *
import random
from src.module.functions import loadconfig

def Main():
    mc = Minecraft()
    modulenm = "GoCrazy"
    configs = loadconfig()['modules'][modulenm]
    player = mc.getPlayerId()
    crazyamount = configs['crazyamount']
    if crazyamount < 1:
        crazyamount = int(crazyamount*10)
        under1 = True
    else:
        crazyamount = int(crazyamount)
        under1 = False

    def gostupid():
        if under1:
            return ((random.randint(1, crazyamount))/10)
        else:
            return random.randint(1, crazyamount)

    while True:
        pos = mc.entity.getPos(player)
        yaw = mc.entity.getRotation(player)
        move = False

        if input.wasPressedSinceLast(input.KEY_W):
            pos.z -= gostupid() * sin(radians(yaw))
            pos.x -= gostupid() * cos(radians(yaw))
            pos.z += gostupid() * sin(radians(yaw))
            pos.x += gostupid() * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.KEY_S):
            pos.z += gostupid() * sin(radians(yaw))
            pos.x += gostupid() * cos(radians(yaw))
            pos.z -= gostupid() * sin(radians(yaw))
            pos.x -= gostupid() * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.KEY_D):
            pos.x += gostupid() * -sin(radians(yaw))
            pos.z += gostupid() * cos(radians(yaw))
            pos.x -= gostupid() * -sin(radians(yaw))
            pos.z -= gostupid() * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.KEY_A):
            pos.x -= gostupid() * -sin(radians(yaw))
            pos.z -= gostupid() * cos(radians(yaw))
            pos.x += gostupid() * -sin(radians(yaw))
            pos.z += gostupid() * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.SPACE):
            posorneg = random.randint(1,2)
            if posorneg == 1:
                pos.y += gostupid()
            else:
                pos.y -= gostupid()
            move = True
        if move:
            try:
                mc.entity.setPos(player,pos)
            except:
                mc.postToChat("Error with "+modulenm)


if __name__ == '__main__':
    Main()