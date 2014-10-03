import pygame
from visual import *


# ventana VPython
scene.width = 800
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================
ground = box(pos=(47, 0, 0), size=(400, 6, 200), color = color.blue)	# piso en VPython

nR = 5 # numero de robots

robot = cylinder(pos=(30,3,0),axis =(0,6,0),radius=10 , color = color.red)