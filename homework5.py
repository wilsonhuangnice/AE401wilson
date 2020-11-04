
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

key = input('enter key word:')
if key == 'house':
   x,y,z = mc.player.getTilePos()
   mc.setBlocks(x+30,y+5,z+30,x-30,y-5,z-30,20)



   mc.setBlocks(x+15,y+3,z+15,x-15,y,z,0) 
  
    


    



