import random as RA
import math
from visual import *


# ventana VPython
scene.width = 800
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================
width = 400
height = 200
ground = box(pos=(200, 0, 100), size=(400, 6, 200), color = color.blue)	# piso en VPython

nR = 5 # numero de robots

def movRobots():
	for i in range(nR):
		robot[i].x += math.cos(robot[i].theta)*robot[i].velocity
		robot[i].z += math.sin(robot[i].theta)*robot[i].velocity
	return
def bounce():
	for i in range(nR):
		if robot[i].x >= width-robot[i].radius:
			robot[i].x -=  (robot[i].x +robot[i].radius)-width
			robot[i].theta = - robot[i].theta
			print robot[i].theta
		elif robot[i].x < robot[i].radius:
			robot[i].x +=  robot[i].radius-robot[i].x
			robot[i].theta = -robot[i].theta
		if robot[i].z > height-robot[i].radius:
			robot[i].z -=  (robot[i].z +robot[i].radius) -height
			robot[i].theta = math.pi + robot[i].theta
		elif robot[i].z < robot[i].radius:
			robot[i].z +=  robot[i].radius-robot[i].z
			robot[i].theta = math.pi - robot[i].theta
	return
robot = []
for i in range(nR):
	x = RA.randint(10,width-10)
	z = RA.randint(10,height-10)
	print z
	robot.append(cylinder(pos=(x,3,z),axis =(0,6,0),radius=10 , color = color.red))
	robot[i].velocity = RA.random()	# asigna velocidad
	#robot[i].theta = RA.uniform(0,math.pi*2)	# angulo de movimiento
	robot[i].theta = math.pi*.5
	
while 1:
	rate(100)
	movRobots()
	bounce()