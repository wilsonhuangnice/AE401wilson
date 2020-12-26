
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import choice

mineral = [14,15,16,56,73,129]
r = choice(mineral)

myID = mc.getPlayerEntityId('wilson40506')
x,y,z = mc.entity.getTilePos(myID)
mc.setBlock(x,y,z,r)


list2d = [[12,41,14],
          [35,73,86]]
x,y,z = mc.player.getTilePos()
startX = x
for list1d in list2d:
    for i in list1d:
        mc.setBlock(x,y,z,i)
        
        x = x + 1
        
    x = startX
    z = z+1