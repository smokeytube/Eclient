#// TODO: Do not hardcode values in later
from src.main.java.org.Eclient.client.mine import *;
import time;
from src.main.java.org.Eclient.client.input import *;
import math;

class hackwalk:
    def Main():
        mc = Minecraft();
        player = True;
        entity = mc.getPlayerId();
        movevar = 0.5;

        while True:
            pos = mc.entity.getPos(entity);
            yaw = mc.entity.getRotation(entity);
            move = False
            if input.wasPressedSinceLast(input.RSHIFT):
                pos.y += 5;
                move = True;
            if input.wasPressedSinceLast(input.UP):
                pos.x += movevar * -sin(radians(yaw));
                pos.z += movevar * cos(radians(yaw));
                move = True;
            if input.wasPressedSinceLast(input.DOWN):
                pos.x -= movevar * -sin(radians(yaw));
                pos.z -= movevar * cos(radians(yaw));
                move = True;
            if input.wasPressedSinceLast(input.RIGHT):
                pos.z -= movevar * sin(radians(yaw));
                pos.x -= movevar * cos(radians(yaw));
                move = True;
            if input.wasPressedSinceLast(input.LEFT):
                pos.z += movevar * sin(radians(yaw));
                pos.x += movevar * cos(radians(yaw));
                move = True;
            if move:
                mc.entity.setPos(entity,pos);

if __name__ == '__main__':
    hackwalk.Main()
    