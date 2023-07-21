import sys 
sys.path.append("../Controlador")
from Color import Color 
from conexion import Conexion
def insertar(insertar,dato):
	conexion=Conexion.ObtenerConexion()
	cursor= Conexion.ObtenerCursor(conexion)
	cursor.execute(insertar,dato)
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
