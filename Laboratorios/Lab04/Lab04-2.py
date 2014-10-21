# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Grafica una regresion lineal con PyLab e inserta este grafico en un archivo Word,
# ------------------ Ademas agrega datos a Excel e inserta grafico de los datos cargados
# -------------------------------------------------

from numpy import arange, array, ones, random, linalg
from pylab import *
import win32com.client as win32
import os
 
def toWord( ruta):
	word = win32.DispatchEx("Word.Application")	# inicia word
	word.DisplayAlerts = 0
	doc = word.Documents.Add() # crea el doc
	word.Visible = True
	newShape = word.ActiveDocument.Shapes.AddPicture(ruta, False, True)	# agrega la foto al documento	
	return
def toExcel():	
	excel = win32.DispatchEx("Excel.Application")
	
	book = excel.Workbooks.Add()	# crea el libro
	sheet1 = book.Worksheets(1)		# selecciona la hoja de trabajo
	excel.Visible = True			# muestra el excel
	
	sheet1.Cells(1,1).Value='X'
	sheet1.Cells(1,2).Value='Y'
	for i in range(0, len(xi)):		# inserta datos a las celdas
		sheet1.Cells(i+2,1).Value = xi[i]
		sheet1.Cells(i+2,2).Value = y[i]	
	sheet1.Shapes.AddChart() # agrega el grafico
	chart = sheet1.ChartObjects(1).Chart		# selecciona el grafico
	chart.ChartType = -4169		# grafico de dispercion	
	chart.SetSourceData(sheet1.Range("B:B"))		# selecciona datos	
	chart.SeriesCollection(1).Trendlines().Add()	# agrega la regresion (linea de tendencia)
	return
#   tabla 1
xi= arange(1, 31)
A = array([xi, ones(30)])
y = [10, 11, 17, 21, 15, 13, 10, 11, 16, 12, 13, 15, 14, 14, 17, 21, 22, 18, 18, 19, 21, 23, 14, 18, 19, 21, 24, 25, 20, 21] 
#===========================
# regresion lineal 
w = linalg.lstsq(A.T, y)[0] 
line = w[0]*xi+w[1]  		# y' = ax +b
#==============
plot(xi,line,'r--', xi,y,'o')
toExcel()
savefig('C:\\fig.png')	# guarda la foto de la grafica
toWord('C:\\fig.png')
os.remove('C:\\fig.png')	# elimina el archivo creado
show()


