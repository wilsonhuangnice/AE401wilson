


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time

x,y,z = mc.player.getTilePos()

for i in range(20):
    r = random.randrange(1, 5)
    color = random.randrange(0,16)
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,35,color)
        x = x+4
        
    elif r == 2:
        mc.setBlocks(x,y,z,x-10,y,z,35,color)
        x = x-10
        
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+13,35,color)
        z = z+13
        
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-5,35,color)
        z = z-5
        
while True:
    mc.executeCommand('time add 500')
    time.sleep(0.1)
         
    
        
        
        