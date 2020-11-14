

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

    
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit= hits[0]
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        if block == 1:
            mc.setBlock(x,y,z,49)
        
        

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'1','2','3','4')



from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
import random
i = 0
while i < 50:
    pos = mc.player.getPos()
    i = i + 1
    x = pos.x + ranodom.uniform(-20,20)
    y = pos.y + ranodom.uniform(-3,0)
    z = pos.z + ranodom.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,92)
    time.sleep(0.1)


