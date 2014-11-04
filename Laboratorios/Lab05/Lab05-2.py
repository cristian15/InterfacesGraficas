# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Sube a FTP imagenes .JPG con efecto Polaroid
# -------------------------------------------------
from ftplib import FTP
import os
import time

def enviaFTP(ruta, destino):
	ftp = FTP('localhost')
	ftp.login('toor','123456')		# conecta
	print ftp.getwelcome()
	file = open(ruta,'rb')
	ftp.storbinary('STOR '+ destino, file)		# sube el archivo
	time.sleep(.5)
	ftp.quit()
	ftp.close()
	print 'File UP'
	
for files in os.listdir("Imagen/"):
    if files.endswith(".jpg"):
		os.system('convert Imagen/'+files+' -bordercolor white -background black +polaroid Imagen/fotoSu.png')	# efecto polaroid
		enviaFTP("Imagen/fotoSu.png", "/Fotos/"+files[:len(files)-4]+".png")