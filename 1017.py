#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:20:15 2020

@author: michael
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()










x,y,z = mc.player.getTilePos()















from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()


mc.setBlock(x,y+1,z,57)
mc.setBlock(x,y+2,z,57)
mc.setBlock(x,y+3,z,57)
mc.setBlock(x,y+4,z,57)
mc.setBlock(x,y+5,z,57)
mc.setBlock(x,y+6,z,57)
mc.setBlock(x,y+7,z,57)
mc.setBlock(x,y+8,z,57)
mc.setBlock(x,y+9,z,57)
mc.setBlock(x,y+10,z,57)
mc.setBlock(x,y+11,z,57)
mc.setBlock(x,y+12,z,57)
mc.setBlock(x,y+13,z,57)



x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z+1,57)
mc.setBlock(x-1,y,z,57)
mc.setBlock(x+1,y,z,57)
mc.setBlock(x,y,z-1,57)
mc.setBlock(x-1,y,z+1,57)
mc.setBlock(x+1,y,z+1,57)
mc.setBlock(x-1,y,z-1,57)
mc.setBlock(x+1,y,z-1,57)



