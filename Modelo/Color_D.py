import sys 
sys.path.append("../Controlador")
from Color import Color 
from conexion import Conexion
from funciones import * 
import pandas as pd
SELECCIONAR='SELECT * FROM color'
ELIMINAR='DELETE FROM color WHERE id_color=?'
INSERTAR='INSERT INTO  color(id_color,color) VALUES(?,?)'
MODIFICAR="UPDATE color set color=? where id_color=?"
class Color_D():
	def insertar(inserta,dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(inserta,dato)
		conexion.commit()
		print("el registro se guardo")
		conexion.close()
	def modificar(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(MODIFICAR,dato)
		conexion.commit()
		print("el registro se actualizo")
		conexion.close()	
	def eliminar(dato):
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(ELIMINAR,dato)
		conexion.commit()
		print("el registro se ELIMINO")
		conexion.close()

	def consultar():
		conexion=Conexion.ObtenerConexion()
		cursor= Conexion.ObtenerCursor(conexion)
		cursor.execute(SELECCIONAR)
		dato=cursor.fetchall()
		conexion.commit()
		conexion.close()
		return dato				

if __name__=='__main__':
	colo=Color(21,"blue claro")
	dato=(colo.id_color,colo.color)
	Color_D.insertar(INSERTAR,dato)
	