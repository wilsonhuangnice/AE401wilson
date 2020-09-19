#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:28:45 2020

@author: michael
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

mc.postToChat("i am watching")

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("X:"+str(x)+"Y:"+str(y)+"Z:"+str(z))





