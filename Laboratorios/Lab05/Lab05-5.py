import os

os.mkdir("Imagenes/Rotaciones")		# crea el directorio para las fotos rotadas
for i in range(1,360):
	os.system("convert Imagenes/foto.png -rotate "+str(i)+" Imagenes/Rotaciones/foto_"+str(i)+".png")
print "Fin de rotacion"