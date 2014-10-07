from visual import *

# ventana VPython
scene.width = 1200
scene.height = 700
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================

height = 200
width = 500
g = -9.8

Robot = frame()
cylinder(frame=Robot,pos=(0,0,0),axis=(8,0,0),radius=10,color=(0,0,255))
cylinder(frame=Robot,pos=(3,0,0),axis=(2,0,0),radius=11,color=(255,255,0))
cone(frame=Robot,pos=(-3,0,0),axis=(4,0,0),radius=4,color=(150,150,150))
Robot.axis=(0,1,0)  # robot apunta hacia arriba
	
Robot.pos = vector(20.0,6.0,20.0)
Robot.vel = vector(0.0,0.0,0.0)
Robot.angleZX = 0.0
Robot.angleYX = 0.0
Robot.masa = 1.0
Robot.Force = 0.0
Robot.fuel = 1000		# combustible


base = box(pos=(20, 0, 20), size=(40,6,40), color=color.red)
ground = box(pos=(width/2, -3, height/2), size=(width, 3, height), color = color.green)	# piso en VPython

Fthru = 0.0

#------ Etiquetas ---------------
Lvelocidad = label(pos = (0, 20, height), text = "Velocidad " + str(Robot.vel), opacity = .5)
LEmpuje = label(pos = (0, 40, height), text = "Empuje " + str(Fthru), opacity = .5)
LAngleYX = label(pos = (0, 60, height), text = "Angulo YX " + str(Robot.angleYX), opacity = .5)
LAngleZX = label(pos = (0, 80, height), text = "Angulo ZX " + str(Robot.angleZX), opacity = .5)
LFuel = label(pos = (0, 100, height), text = "Combustible " + str(Robot.fuel), opacity = .5)
#--------------------------------

Fg = vector(0.0, g, 0.0) * Robot.masa		# calcula Peso
dt = .01
pointer = arrow(pos=(0,0,0), axis= Robot.axis*100, shaftwidth =5, color= color.orange)	# dibuja Vector direccion



while True:
	rate(100)
	# ------------- Calcula angulos de direccion ------------------
	if Robot.axis.z != 0:
		# ---------   Primer cuadrante ---------------------
		Robot.angleZX = round(abs(math.degrees( math.atan(Robot.axis.x/Robot.axis.z))), 3) 
		# --------------------------------------------------
		if Robot.axis.x > 0:
			# ----------  segundo cuadrante  X > 0 y Z < 0 ----------------
			if Robot.axis.z < 0:
				Robot.angleZX = 180 - Robot.angleZX 
			# ---------------------------------------------------------
			
		elif Robot.axis.x < 0:
			# ------------------ Terces cuadrante ---------------------
			if Robot.axis.z < 0:
				Robot.angleZX += 180
			# ---------------------------------------------------------
			# ------------------ Cuarto Cuadrante ---------------------
			elif Robot.axis.z > 0:
					Robot.angleZX = 360 - Robot.angleZX
			# ---------------------------------------------------------
	else: # si z es Zero
		if Robot.axis.x > 0:
			Robot.angleZX = 90
		elif Robot.axis.x < 0:
			Robot.angleZX = 270
			
			
	if Robot.axis.x != 0:
		Robot.angleYX = 90-round(abs(math.degrees( math.atan(Robot.axis.y/Robot.axis.x))), 3)		
		if Robot.axis.y < 0:
			Robot.angleYX = 180 - Robot.angleYX		
	else: # si x es Zero
		if Robot.axis.z > 0:
			Robot.angleZX = 0
		elif Robot.axis.z < 0:
			Robot.angleZX = 180
	# -----------------------------------------------------------------
	# -------------- Coordenadas esfericas ----------------------------
	x = Robot.Force * math.sin( math.radians( Robot.angleYX ) ) * math.sin( math.radians( Robot.angleZX ) )
	y = Robot.Force * math.cos( math.radians( Robot.angleYX ) )
	z = Robot.Force * math.sin( math.radians( Robot.angleYX ) ) * math.cos( math.radians( Robot.angleZX ) )
	# -----------------------------------------------------------------
	
	Fthru = vector( x, y, z )		# Empuje
	Fnet = Fthru + Fg
	Robot.vel += ( Fnet/Robot.masa ) * dt
	Robot.pos += Robot.vel * dt		# actualiza pos
	Robot.fuel -= abs(Robot.vel.x + Robot.vel.y + Robot.vel.z )*.1 * dt	# disminuye combustible
	
	#------ Etiquetas ---------------
	Lvelocidad.text = "Velocidad " + str(round(Robot.vel.x,3)) + ", "+ str(round(Robot.vel.y,3)) + ", " + str(round(Robot.vel.z,3)) +">"
	LEmpuje.text = "Empuje < " + str(round(Fthru.x,3)) + ", "+ str(round(Fthru.y,3)) + ", " + str(round(Fthru.z,3)) +">"
	LAngleYX.text = "Angulo YX " + str(Robot.angleYX)
	LAngleZX.text = "Angulo ZX " + str(Robot.angleZX)
	LFuel.text = "Combustible " + str(Robot.fuel)
	#--------------------------------
	
	print Robot.axis
	# ------------------ Vector de direccion Empuje --------------------
	pointer.axis= vector(Robot.axis.x, Robot.axis.y, Robot.axis.z)*100  
	# ------------------------------------------------------------------
	
	if Robot.x <= base.x + base.width  and Robot.z <= base.z +base.height:	# si esta sobre la base
		if Robot.y <= 6.0:  # acota piso
			Robot.y = 6.0
			Robot.vel = vector(0.0, 0.0, 0.0)
			Fthru = vector(0.0, 0.0, 0.0)
	else:		# si no esta sobre la base
		if Robot.y <= 0.0:  # acota piso
			Robot.y = 0.
			Robot.vel = vector(0.0, 0.0, 0.0)
			Fthru = vector(0.0, 0.0, 0.0)
		
	# ---------- Limites --------------------
	if Robot.x >= width:	# no avanza fuera de la pista
		Robot.x = width	
	elif Robot.x <=0.0:
		Robot.x = 0.0
	if Robot.z >= height:
		Robot.z = height
	elif Robot.z <= 0:
		Robot.z =0		
	if Robot. y > 200.0:
		Robot.y = 200.0
	# ---------------------------------------
	if scene.kb.keys:
		k = scene.kb.getkey()
		if k == 'u':
			Robot.Force += .5
			print Robot.Force
		if k == 'r':
			Robot.Force = 0.0
			Robot.axis = vector(0,1,0)
		if k == 'right':
			#Robot.angleYX += 1	
			Robot.rotate(angle = math.radians(-1), axis=(0,1,0), origin=Robot.pos) 	# gira el dron
			print Robot.angleYX
		if k == 'left':
			#Robot.angleYX += 1
			Robot.rotate(angle = math.radians(1), axis=(0,1,0), origin=Robot.pos)
		if k == 'down':
			#Robot.angleZX -= 1
			Robot.rotate(angle = math.radians(1), axis=(0,0,1), origin=Robot.pos)
			print Robot.angleZX
		if k == 'up':
			#Robot.angleZX -= 1
			Robot.rotate(angle = math.radians(-1), axis=(0,0,1), origin=Robot.pos)
			
			
			
			
			