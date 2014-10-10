from visual import *
import wiiuse 
import serial

# ------------ ventana VPython
scene.width = 1000
scene.height = 600
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#--------------------------------


width = 600
height = 200
angle = 13
g = -9.8
dt = 0.01

TablaBloque = frame()

ground = box( pos=(0, -3, 0), size=(width, 6, height), color = color.green)	# piso en VPython

tabla = box(frame=TablaBloque, pos = (0, 40, 0), size = (300, 10, height/2), color = color.red)
tabla.mu = 1
#tabla.rotate(angle=-math.radians(angle), axis = (0,0,1))

p1 = box(pos = (0, 25, 60), size = (40, 50, 20))
p2 = box(pos = (0, 25, -60), size = (40, 50, 20))

bloque = box(frame= TablaBloque,pos=(0, 55,0), size=(40,20,20), color=color.blue)
#bloque.rotate(angle=-math.radians(angle), axis = (0,0,1))
bloque.masa = 1
bloque.Vy = 0.0
bloque.Vx = 0.0
TablaBloque.rotate(angle=-math.radians(angle), axis = (0,0,1))

bloque.Fg = bloque.masa * g
bloque.Fn = bloque.masa*g*math.sin(math.radians(angle))
def moveBloque():
	a = bloque.Fg* math.sin(math.radians(-angle))	
	bloque.Vx = a*dt
	bloque.x += bloque.Vx*dt/100
	if bloque.x > (tabla.length -bloque.length)/2: # Borde de la tabla
		bloque.x = (tabla.length -bloque.length)/2
	if bloque.x < -(tabla.length -bloque.length)/2:
		bloque.x = -(tabla.length -bloque.length)/2 
	print bloque.x

b = 0
wiimots = wiiuse.init(1)
encontrado = wiiuse.find(wiimots, 1, 5)
connected = wiiuse.connect(wiimots, 1)

wiiuse.set_leds(wiimots[0], wiiuse.LED[2])
wiiuse.rumble(wiimots[0],0)
sleep(1)


s = serial.Serial(9)		# COM8 virtual
s.baudrate = 9600

s.timeout = 0		# no espera a leer
alp = 0.0
while 1:
	#WiiMo(wiimotes[0])		
	#Wiis.an()
	alpha  = s.readline()
	
	try:
		alp = float(alpha)/100	
	except:
		print alp
	print alp
	
	rate(100)
	dt += 0.01		
	if b == 1:
		moveBloque()	
	if scene.kb.keys:					
		k = scene.kb.getkey()
		if k == 's':		# soltar bloque
			b = 1
		if k == 'up':
			if angle < 13:
				angle += 1		# mueve la tabla un grado
				TablaBloque.rotate(angle = -math.radians(1), axis = (0,0,1))				
		if k == 'down':
			if angle > -13:
				angle -= 1
				TablaBloque.rotate(angle=-math.radians(-1), axis = (0,0,1))
	if angle+alp <= 13 and angle+alp >=-13:
		TablaBloque.rotate(angle = math.radians(-alp), axis = (0,0,1))
		angle += alp
	alp = 0.0