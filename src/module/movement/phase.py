# /py src/module/movement/phase

import input as input
from mine import *
from mcpi.minecraft import *
from src.module.functions import loadconfig

def Main():
    mc = Minecraft()
    modulenm = "Phase"
    configs = loadconfig()['modules'][modulenm]
    player = mc.getPlayerId()
    Yspeed = configs['phaseamount']

    while True:
        pos = mc.entity.getPos(player)
        move = False
        if input.wasPressedSinceLast(input.KEY_PLUS):
            pos.y += Yspeed
            move = True
        if input.wasPressedSinceLast(input.KEY_MINUS):
            pos.y -= Yspeed
            move = True
        if move:
            try:
                mc.entity.setPos(player,pos)
            except:
                mc.postToChat("Error")


if __name__ == '__main__':
    Main()
    