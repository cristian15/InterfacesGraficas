from visual import *

# ventana VPython
scene.width = 800
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================
width = 600
height = 200
posInicial=(30,300,100)
ground = box(pos=(width/2, 0, height/2), size=(width, 6, height), color = color.blue)	# piso en VPython

ball = sphere(pos=posInicial, radius=20, color=color.green)