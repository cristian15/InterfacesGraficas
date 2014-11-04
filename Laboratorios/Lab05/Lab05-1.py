# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Convierte y agrega efectos a fotos con ImageMagick
# -------------------------------------------------
import os

# --------------- Convierte Formatos --------------
os.system("convert Imagen/foto.bmp Imagen/foto.jpg")
os.system("convert Imagen/foto.bmp Imagen/foto.gif")
os.system("convert Imagen/foto.bmp Imagen/foto.tiff")
os.system("convert Imagen/foto.bmp Imagen/foto.png")
# --------------------------------------------------

# ----------------------- Resize ---------------------- 
os.system("convert Imagen/foto320x256.jpg -background black -gravity center -resize 640x480 -extent 640x480 Imagen/foto640x480.jpg")
os.system("convert Imagen/foto320x256.jpg -background black -gravity center -resize 200x100 -extent 200x100 Imagen/foto200x100.jpg")
os.system("convert Imagen/foto320x256.jpg -background black -gravity center -resize 1280x800 -extent 1280x800 Imagen/foto1280x800.jpg")
# -------------------------------------------------------

# ----------- Borders ------------------------------
os.system("convert Imagen/foto.png -bordercolor white -border 3x3 Imagen/fotoB3x3.jpg")
os.system("convert Imagen/foto.png -bordercolor white -border 4x5 Imagen/fotoB4x5.jpg")
os.system("convert Imagen/foto.png -bordercolor white -border 10x8 Imagen/fotoB10x8.jpg")

os.system("convert Imagen/foto.png -bordercolor red -border 3x3 Imagen/fotoB3x3.jpg")
os.system("convert Imagen/foto.png -bordercolor red -border 4x5 Imagen/fotoB4x5.jpg")
os.system("convert Imagen/foto.png -bordercolor red -border 10x8 Imagen/fotoB10x8.jpg")

os.system("convert Imagen/foto.png -bordercolor blue -border 3x3 Imagen/fotoB3x3.jpg")
os.system("convert Imagen/foto.png -bordercolor blue -border 4x5 Imagen/fotoB4x5.jpg")
os.system("convert Imagen/foto.png -bordercolor blue -border 10x8 Imagen/fotoB10x8.jpg")

os.system("convert Imagen/foto.png -bordercolor green -border 3x3 Imagen/fotoB3x3.jpg")
os.system("convert Imagen/foto.png -bordercolor green -border 4x5 Imagen/fotoB4x5.jpg")
os.system("convert Imagen/foto.png -bordercolor green -border 10x8 Imagen/fotoB10x8.jpg")

# ----------------------------------------------------

# ------------- wave -----------------
os.system("convert Imagen/foto.jpg -wave 10x100 Imagen/fotoWave.jpg")
# ----------------------------------------------------------

# ----------------------------- Gradientes -------------------------------
os.system("convert xc:red xc:green xc:blue +append -gravity center -resize 640x480 -extent 640x480 Imagen/foto.png")
os.system("convert Imagen/foto.png -bordercolor white -background black +polaroid Imagen/fotoPolaroid.png")

os.system("convert -size 100x100 radial-gradient:blue-black Imagen/radialB.png")
os.system("convert -size 100x100 radial-gradient:green Imagen/radialG.png")
os.system("convert -size 100x100 radial-gradient:red Imagen/radialR.png")