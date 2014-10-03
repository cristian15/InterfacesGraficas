import random as RA
from visual import *


# ventana VPython
scene.width = 800
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================
ground = box(pos=(0, 0, 0), size=(400, 6, 200), color = color.blue)	# piso en VPython

nR = 5 # numero de robots

for i in range(0, nR):
	x = RA.randint(10,200)
	z = RA.randint(10,100)
	robot[i] = cylinder(pos=(x,3,z),axis =(0,6,0),radius=10 , color = color.red)