#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 09:46:00 2020

@author: michael
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=67
y=200
z=330

mc.player.setTilePos(x,y,z)