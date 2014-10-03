import random as RA
from visual import *


# ventana VPython
scene.width = 800
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================
ground = box(pos=(200, 0, 100), size=(400, 6, 200), color = color.blue)	# piso en VPython

nR = 5 # numero de robots

def movRobots():
	
	return
robot = []
for i in range(nR):
	x = RA.randint(10,400-10)
	z = RA.randint(10,200-10)
	robot.append(cylinder(pos=(390,3,z),axis =(0,6,0),radius=10 , color = color.red))
	robot[i].vel = RA.random()	# asigna velocidad
	robot[i].theta = RA.randint(0,359)
	
	print robot[i].vel
