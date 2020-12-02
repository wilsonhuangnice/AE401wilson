

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    block = mc.getBlockWithData(x,y-1,z)
    print(block)
    
    if block.data == 11:
        mc.postToChat('TURN RIGHT')
    if block.data == 14:
        mc.postToChat('WATCH OUT!!!!')
    if block.data == 13:
        mc.postToChat('TURN LEFT')
    if block.data == 15:
        mc.postToChat('DEAD END')