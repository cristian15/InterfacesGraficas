import os
from ftplib import FTP
import time

files = []
dirs = []
ftp = FTP('localhost')
ftp.login('toor','123456')		# conecta
print ftp.getwelcome()
#ftp.cwd('/capturas')
ftp.dir(dirs.append)
dirs = ftp.nlst()		# lista de directorios en el FTP
for d in dirs:
	print '/'+d
	ftp.cwd('/'+d)	# entra al directorio ftp	
	for f in ftp.nlst():
		files.append(d+'/'+f)		# ruta completa de archivos
try:
	os.mkdir('fotosFTP')
except:
	print "Carpeta ya existe"
i = 0
for f in files:
	ftp.retrbinary('RETR /'+f, open('foto.png','wb').write)		# sube el archivo	
	os.system('convert foto.png -bordercolor white -background black +polaroid -thumbnail 640x480 fotosFTP/fotoPol_'+str(i)+'.jpg')	# efecto polaroid
	print f
	i += 1
time.sleep(.5)
ftp.quit()
ftp.close()