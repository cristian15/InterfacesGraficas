# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Rota una imagen cada grado y la guarda con ImageMagick
# -------------------------------------------------
import os

os.mkdir("Imagen/Rotaciones")		# crea el directorio para las fotos rotadas
for i in range(1,360):
	os.system("convert Imagen/fotos.png -rotate "+str(i)+" Imagen/Rotaciones/foto_"+str(i)+".png")
print "Fin de rotacion"