#//This module isn't finished yet. Please check later


from src.main.java.org.Eclient.client.mine import *;
import time;
from src.main.java.org.Eclient.client.input import *;
import math;

mc = Minecraft();
player = True;

movevar = 0.5;

while True:
    entitys = mc.getPlayerEntityIds();
    player = mc.getPlayerId();
    posentity = mc.entity.getPos(entitys[0]);
    posplayer = mc.entity.getPos(player);
    diffx = posentity.x - posplayer.x;
    diffy = posentity.y - posplayer.y;
    diffz = posentity.z - posplayer.z;
    
    chatmsg = (mc.entity.getName(entitys[0]));
    mc.postToChat(chatmsg);
    mc.postToChat(math.sqrt((diffx ** 2) + (diffz ** 2)));

    time.sleep(1);
    