# /py src/module/movement/speed

import input as input
from mine import *
from mcpi.minecraft import *
from src.module.functions import loadconfig

def Main():
    mc = Minecraft()
    modulenm = "Speed"
    configs = loadconfig()['modules'][modulenm]
    player = mc.getPlayerId()
    moveamount = configs['travelspeed']

    while True:
        pos = mc.entity.getPos(player)
        yaw = mc.entity.getRotation(player)
        move = False
        if input.wasPressedSinceLast(input.UP):
            pos.x += moveamount * -sin(radians(yaw))
            pos.z += moveamount * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.DOWN):
            pos.x -= moveamount * -sin(radians(yaw))
            pos.z -= moveamount * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.RIGHT):
            pos.z -= moveamount * sin(radians(yaw))
            pos.x -= moveamount * cos(radians(yaw))
            move = True
        if input.wasPressedSinceLast(input.LEFT):
            pos.z += moveamount * sin(radians(yaw))
            pos.x += moveamount * cos(radians(yaw))
            move = True
        if move:
            try:
                mc.entity.setPos(player,pos)
            except:
                mc.postToChat("Error with "+modulenm)


if __name__ == '__main__':
    Main()