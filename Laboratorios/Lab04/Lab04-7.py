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
g = -9.8
dt=.01
ground = box(pos=(width/2, -1, height/2), size=(width, 2, height), color = color.blue)	# piso en VPython


ball = sphere(pos=posInicial, radius=2, color=color.green)
ball.masa = 10 	# masa 10 kg
ball.velocity = vector(0,0,0)
ball.E = abs(ball.masa*g*posInicial.y/100)  # Energia potencial gravitatoria
ball.epsilon = .7 # coeficiente de restitucion

h0= posInicial.y
h1=posInicial.y
wind = vector(30, -1, 5)



s = 0	
while 1:
	rate(100)	
	if s == 1:
		if ball.y > ball.radius and dir == 1:		# en bajada
			ball.velocity.y += g*dir
			ball.y += (wind.y + ball.velocity.y) * dt
			ball.x += wind.x*dt
			ball.z += wind.z*dt
		if ball.y < h1-ball.radius and dir == -1:		# en subida
			ball.velocity.y += g*dir
			ball.y += (wind.y + ball.velocity.y) * dt
			ball.x += wind.x * dt
			ball.z += wind.z * dt
		if ball.y >= h1 - ball.radius and dir == -1:    # llega a la altura de rebote
			ball.y = h1
			dir = 1
		if ball.y <= ball.radius and dir == 1:		# llega al suelo
			ball.y = ball.radius
			dir = -1		# cambia a subida
			h1 = h0*ball.epsilon**2		# calcula altura del rebote
			h0=h1						#
			ball.velocity.y = math.sqrt(2*ball.E/ball.masa)
			ball.E = abs(ball.masa*g*h1/100)
			ball.pos += ball.velocity 
			
	if scene.kb.keys:
		k = scene.kb.getkey()
		if k == 's':		# soltar bloque
			s = 1
		if k == 'r':
			s = 0
			dir = 1
			h0= posInicial.y
			h1=posInicial.y
			ball.pos = posInicial
		