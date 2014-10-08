from visual import *
import wiiuse

# ventana VPython
scene.width = 1000
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================

width = 600
height = 200
angle = 10
g = -9.8
dt = 0.01

ground = box(pos=(0, -3, 0), size=(width, 6, height), color = color.green)	# piso en VPython

tabla = box(pos = (0, 40, 0), size = (300, 10, height/2), color = color.red)
tabla.rotate(angle=-math.radians(angle), axis = (0,0,1))

p1 = box(pos = (0, 25, 60), size = (40, 50, 20))
p2 = box(pos = (0, 25, -60), size = (40, 50, 20))

bloque = box(pos=(0, 55,0), size=(40,20,20), color=color.blue)
bloque.rotate(angle=-math.radians(angle), axis = (0,0,1))
bloque.masa = 1
bloque.Vy = 0.0
bloque.Vx = 0.0
while 1:
	rate(100)
	if angle < 0:
		bloque.Vy = math.sin(math.radians(-angle))*g*bloque.masa
		bloque.Vx = math.cos(math.radians(-angle))*g*bloque.masa
	elif angle > 0:
		bloque.Vy = -math.sin(math.radians(-angle))*g*bloque.masa
		bloque.Vx = -math.cos(math.radians(-angle))*g*bloque.masa
	bloque.x += bloque.Vx*dt
	bloque.y += bloque.Vy*dt
	
	if scene.kb.keys:
		k = scene.kb.getkey()
		if k == 's':		# soltar bloque
			bloque.Vy = math.cos(math.radians(angle))*g*bloque.masa
			bloque.Vx = math.sin(math.radians(angle))*g*bloque.masa
		
			
			
			
			