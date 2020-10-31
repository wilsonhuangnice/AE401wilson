


from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z = mc.player.getTilePos()




a = 10
b = 6
c = 5

mc.setBlocks(x, y, z, x+a, y+b, z+c, 57)
mc.setBlocks(x+1, y+1, z+1, x+a-1, y+b-1, z+c-1, 0)

b = input('enter block high')
          








try:
    a = int(input('enter blockid:'))    
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,a)
except:
    print('error')