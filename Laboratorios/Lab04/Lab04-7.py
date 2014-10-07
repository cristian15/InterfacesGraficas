from visual import *

# ventana VPython
scene.width = 800
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================
width = 100
height = 40
posInicial = vector(5,50,height/2)
dir = 1
g = 9.8
dt=.01
ground = box(pos=(width/2, -1, height/2), size=(width, 1, height), color = color.blue)	# piso en VPython


ball = sphere(pos=posInicial, radius=2, color=color.green)
ball.masa = 10 	# masa 10 kg
ball.velocity = vector(0,0,0)
ball.E = ball.masa*g*posInicial.y  # Energia potencial gravitatoria
ball.epsilon = .7 # coeficiente de restitucion

h0= posInicial.y
h1=0
while 1:
	rate(100)
	
	if ball.y > ball.radius:
		ball.velocity.y += -g*dt*dir
		ball.pos += ball.velocity
		ball.x += .2
		
	if ball.y <= ball.radius:
		di=-1
		h1 = h0*ball.epsilon**2	
		h0=h1
		
		