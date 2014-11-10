# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Envia por serial datos de un joystick
# -------------------------------------------------
import pygame
import serial
import time
from pygame import locals

pygame.init()
pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()

s = serial.Serial(4)		# COM5 virtual
s.baudrate = 2400
print j.get_name()
while 1:
	for e in pygame.event.get(): 
		if e.type == pygame.locals.JOYAXISMOTION: # 7
			x , y = round(j.get_axis(0), 3), round(j.get_axis(1),3)
			#print '[x , y] : ' + str(x) +' , '+ str(y)
			s.write(str(10*x)+' '+ str(10*y))
			#print str(10*x)+' '+str(10*y)
			time.sleep(.1)
		elif e.type == pygame.locals.JOYBUTTONDOWN: # 10
			if j.get_button(4):	# button L1
				print 'L1'
				s.write('L1')
			if j.get_button(11):	# button Start
				print 'START'
				s.write('START')
			if j.get_button(5):	# button L1
				print 'R1'
				s.write('R1')
			
			time.sleep(.1)