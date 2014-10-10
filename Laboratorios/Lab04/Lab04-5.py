from visual import *
import random as RA

# ventana VPython
scene.width = 1200
scene.height = 700
scene.autocenter = True
scene.autoscale = True
scene.background = (255,255,255)
#=================

height = 400
width = 800
g = -9.8
fuelInitial = 1000.0
nDrons = 5
def createRobot():
	Robot = frame()	
	cylinder( frame=Robot,pos=(0,0,0),axis=(8,0,0),radius=10,color=color.blue )
	cylinder( frame=Robot,pos=(3,0,0),axis=(2,0,0),radius=11,color=(255,255,0) )
	cone( frame=Robot,pos=(-3,0,0),axis=(4,0,0),radius=4,color=(150,150,150) )
	Robot.axis=( 0, 1, 0 )  # robot apunta hacia arriba
	xIni = RA.randint(20, width-20)
	zIni = RA.randint(20, height-20)	
	
	Robot.pos = vector(xIni,6.0,zIni)
	Robot.vel = vector(0.0,0.0,0.0)
	# ------- Angulos coordenadas esfericas
	Robot.angleZX = 0.0		
	Robot.angleYX = 0.0
	# ----------------------------------
	Robot.masa = 1.0
	Robot.Force = RA.uniform(12, 18)
	Robot.fuel = fuelInitial		# combustible
	Robot.Thru = 0.0
	Robot.Fg = vector(0.0, g, 0.0) * Robot.masa		# calcula Peso
	Robot.axis = vector(RA.uniform(-0.3,0.3),RA.uniform(0,1),RA.uniform(-0.3,0.3))
	
	Robot.base = box(pos =(xIni, 0,zIni), size=(40,6,40), color= color.red)
	
	#------ Etiquetas ---------------
	#Robot.Lvelocidad = label(pos = (Robot.x,Robot.y,Robot.z), text = "Velocidad " + str(Robot.vel), opacity = .5)
	#Robot.LEmpuje = label(pos = (Robot.x,Robot.y+20,Robot.z), text = "Empuje " + str(Robot.Thru), opacity = .5)
	Robot.LFuel = label(pos = (Robot.x,Robot.y+40,Robot.z), text = "Combustible " + str(Robot.fuel), opacity = .1)
	#--------------------------------	
	return Robot
	
def setAngles():
	for i in range(len(dron)):
		if dron[i].axis.z != 0:
			# ---------   Primer cuadrante ---------------------
			dron[i].angleZX = round(abs(math.degrees( math.atan(dron[i].axis.x/dron[i].axis.z))), 3) 
			# --------------------------------------------------
			if dron[i].axis.x > 0:
				# ----------  segundo cuadrante  X > 0 y Z < 0 ----------------
				if dron[i].axis.z < 0:
					dron[i].angleZX = 180 - dron[i].angleZX 
				# ---------------------------------------------------------
				
			elif dron[i].axis.x < 0:
				# ------------------ Terces cuadrante ---------------------
				if dron[i].axis.z < 0:
					dron[i].angleZX += 180
				# ---------------------------------------------------------
				# ------------------ Cuarto Cuadrante ---------------------
				elif dron[i].axis.z > 0:
						dron[i].angleZX = 360 - dron[i].angleZX
				# ---------------------------------------------------------
		else: # si z es Zero
			if dron[i].axis.x > 0:
				dron[i].angleZX = 90
			elif dron[i].axis.x < 0:
				dron[i].angleZX = 270			
				
		if dron[i].axis.x != 0:
			dron[i].angleYX = 90-round(abs(math.degrees( math.atan(dron[i].axis.y/dron[i].axis.x))), 3)		
			if dron[i].axis.y < 0:
				dron[i].angleYX = 180 - dron[i].angleYX		
		else: # si x es Zero
			if dron[i].axis.z > 0:
				dron[i].angleZX = 0
			elif dron[i].axis.z < 0:
				dron[i].angleZX = 180
		# -----------------------------------------------------------------
		dron[i].angleYX
	return
	
def movDron(Robot):
	# -------------- Coordenadas esfericas ----------------------------
	x = Robot.Force * math.sin( math.radians( Robot.angleYX ) ) * math.sin( math.radians( Robot.angleZX ) )
	y = Robot.Force * math.cos( math.radians( Robot.angleYX ) )
	z = Robot.Force * math.sin( math.radians( Robot.angleYX ) ) * math.cos( math.radians( Robot.angleZX ) )
	# -----------------------------------------------------------------
	
	# ------------ Actualiza variables de vuelo ---------------------
	Robot.Thru = vector( x, y, z )		# Empuje
	Fnet = Robot.Thru + Robot.Fg
	Robot.vel += ( Fnet/Robot.masa ) * dt
	Robot.pos += Robot.vel * dt		# actualiza pos
	Robot.fuel -= abs(Robot.vel.x + Robot.vel.y + Robot.vel.z )*.1 * dt	# disminuye combustible
	# -----------------------------------------------------------------
	
	# ---------------- Combustible --------------------
	if Robot.fuel <= 0.0:  # se acaba el combustible
		Robot.fuel = 0.0
		Robot.Force = 0.0
	
	if Robot.fuel <= fuelInitial*.25:
		Robot.axis = vector(Robot.base.x, 1, Robot.base.z)
		if Robot.x <= Robot.base.x :
			Robot.axis.x = 0
		if Robot.z <= Robot.base.z:
			Robot.axis.z = 0 
		if Robot.x <= Robot.base.x and Robot.z <= Robot.base.z:
			Robot.axis = (0,1,0)
			Robot.Force = 9.4
	# -------------------------------------------------
	
	#------ Etiquetas ---------------
	#Robot.Lvelocidad.text = "Velocidad " + str(round(Robot.vel.x,3)) + ", "+ str(round(Robot.vel.y,3)) + ", " + str(round(Robot.vel.z,3)) +">"
	#Robot.LEmpuje.text = "Empuje < " + str(Robot.Thru) 
	Robot.LFuel.text = "Combustible " + str(round(Robot.fuel, 3)) + " Lts. ("+str(round(Robot.fuel*100/fuelInitial,2))+" %)"
	#--------------------------------
	return
# -------------- Crea los drones ---------
dron = []
for i in range(nDrons):
	dron.append(createRobot())		# agrega los drones al arreglo
# ---------------------------------------
setAngles()
dt = 0.01
ground = box(pos=(width/2, -3, height/2), size=(width, 3, height), color = color.green)	# piso en VPython

while 1:
	rate(100)
	setAngles()
	for i in range(len(dron)):
		movDron(dron[i])		# mueve el dron
		# ---------- Limites --------------------
		if dron[i].x <= dron[i].x + dron[i].base.width  and dron[i].z <= dron[i].base.z +dron[i].base.height:	# si esta sobre la base del dron
			if dron[i].y <= 6.0:  # acota piso
				dron[i].y = 6.0
				dron[i].vel = vector(0.0, 0.0, 0.0)
				Fthru = vector(0.0, 0.0, 0.0)
		else:		# si no esta sobre la base
			if dron[i].y <= 0.0:  # acota piso
				dron[i].y = 0.0
				dron[i].vel = vector(0.0, 0.0, 0.0)
				Fthru = vector(0.0, 0.0, 0.0)
		if dron[i].x >= width:	# no avanza fuera de la pista
			dron[i].x = width	
		elif dron[i].x <=0.0:
			dron[i].x = 0.0
		if dron[i].z >= height:
			dron[i].z = height
		elif dron[i].z <= 0:
			dron[i].z =0		
		if dron[i]. y > 200.0:
			dron[i].y = 200.0
		# ---------------------------------------
	if scene.kb.keys:
		k = scene.kb.getkey()
		if k == 'r':		# cambia direccion
			for i in range(len(dron)):
				dron[i].axis = vector(RA.uniform(-0.5,0.5),RA.uniform(0,1),RA.uniform(-0.5,0.5))
		if k == 'u':		# Aumenta Empuje
			for i in range(len(dron)):
				dron[i].Force += .2
		
		
		
		