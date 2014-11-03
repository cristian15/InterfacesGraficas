import pygame.image
import PIL
from VideoCapture import Device
from ftplib import FTP
import time
import os

(width, height) = (800, 600)
background = (255,255,255)
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scanner')
cam = Device()		# inicia la camara
screen.fill(background)

def enviaFTP(ruta, destino):
	#ftp = FTP('vigilatucasa.cl')
	#ftp.login('vigilatu','[F4z7#y~IQF{')		# conecta
	ftp = FTP('localhost')
	ftp.login('toor','123456')		# conecta
	print ftp.getwelcome()
	file = open(ruta,'rb')
	ftp.storbinary('STOR '+ destino, file)		# sube el archivo
	time.sleep(.5)
	ftp.quit()
	ftp.close()
	print 'File UP'
	
fuente = pygame.font.Font(None, 40)
	# -------------- etiquetas ------------------
etiqueta = fuente.render('Tiempo: 0.0',1, (0,0,0))	
screen.blit(etiqueta, (20, height-55))
cam.saveSnapshot('img.png')	# captura imagen 
os.system("convert -charcoal 3 img.png  imgCar.png")		# efecto carboncillo
enviaFTP('imgCar.png','/capturas/fc_0.png')

tInicio = time.time()
run = True
i = 1
while run:
	even = pygame.event.get()
	cKey = pygame.key.get_pressed()
	screen.fill((255,255,255))
	for e in even:
		if e.type == pygame.QUIT:
			run = False
	image = cam.getImage()		# captura la imagen
	img = pygame.image.fromstring(image.tostring(), image.size, 'RGB')		# convierte a surface la PIL image
	
	tiempo = (time.time() - tInicio)%60  # tiempo transcurrido en seg
	if tiempo > 30.0:
		cam.saveSnapshot('img.png')	# captura imagen 
		os.system("convert -charcoal 3 img.png  imgCar.png")	# efecto carboncillo
		enviaFTP('imgCar.png','/capturas/fc_'+str(i)+'.png')		
		tInicio = time.time()
		i += 1
	etiqueta = fuente.render('Tiempo: '+str(round(tiempo,2)),1, (0,0,0))	
	screen.blit(etiqueta, (20, height-55))
	screen.blit(img, (width/2 - 320,0))
	pygame.display.flip()