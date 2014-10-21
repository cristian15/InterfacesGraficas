# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Scanner con webcam, captura una imagen con una webcam y la guarda en un archivo Word
# -------------------------------------------------
import pygame.image
import PIL
import win32com.client
import os

from VideoCapture import Device

(width, height) = (800, 600)
background = (255,255,255)
pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scanner')
cam = Device()		# inicia la camara
screen.fill(background)

word = win32com.client.DispatchEx("Word.Application")	# inicia word
word.DisplayAlerts = 0
doc = word.Documents.Add() # Crea el doc
fuente = pygame.font.Font(None, 40)
	# -------------- etiquetas ------------------
etiqueta = fuente.render('Capturar[a]        Guardar[s] ',1, (0,0,0))	
screen.blit(etiqueta, (20, height-55))


run = True
while run:
	even = pygame.event.get()
	cKey = pygame.key.get_pressed()
	for e in even:
		if e.type == pygame.QUIT:
			run = False
		if cKey[pygame.K_a]:
			cam.saveSnapshot('c:\\img.png')	# captura imagen 
			newShape = word.ActiveDocument.InlineShapes.AddPicture("c:\\img.png", False, True)	# agrega la foto al documento
			os.remove('c:\\img.png')
		if cKey[pygame.K_s]:
			word.Visible = True	# muestra el documento
	image = cam.getImage()		# captura la imagen
	img = pygame.image.fromstring(image.tostring(), image.size, 'RGB')		# convierte a surface la PIL image
	screen.blit(img, (width/2 - 320,0))
	pygame.display.flip()

