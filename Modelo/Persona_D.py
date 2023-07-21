import sys 
sys.path.append("../Controlador")
from conexion import Conexion
from Personas import Persona 
import pandas as pd
class Persona_D:
	def insertar(INSERTAR,dato):
		conexion=Conexion.ObtenerConexion()
		cursor= conexion.cursor()
		cursor.execute(INSERTAR,dato)
		conexion.commit()
		print("el registro se guardo")
		conexion.close()
	def modificar(MODIFICAR,dato):
		conexion=Conexion.ObtenerConexion()
		cursor= conexion.cursor()
		cursor.execute(MODIFICAR,dato)
		conexion.commit()
		print("el registro se actualizo")
		conexion.close()	
	def eliminar(ELIMINAR,dato):
		conexion=Conexion.ObtenerConexion()
		cursor= conexion.cursor()
		cursor.execute(ELIMINAR,dato)
		conexion.commit()
		print("el registro se ELIMINO")
		conexion.close()
	def consultar(SELECCIONAR):
		conexion=Conexion.ObtenerConexion()
		cursor= conexion.cursor()
		cursor.execute(SELECCIONAR)
		dato=cursor.fetchall()
		conexion.commit()
		conexion.close()
		return dato	
"""					
if __name__ == '__main__':
#	pass
	INSERTAR='INSERT INTO  persona(id_persona,nombre,telefono,email,estado,tipo) VALUES(?,?,?,?,?,?)' 
	persona=Persona(25,"maria",7845214,"picapiedra@gmail.com",0,"propietario")
	dato=[persona.id_persona,persona.nombre,persona.telefono,persona.email,persona.estado,persona.tipo]
	Persona_D.insertar(INSERTAR,dato)
	#dato=(201,)
	#Persona_D.modificar(dato)
	#Persona_D.eliminar(dato)
	#dato=(201,)
	SELECCIONAR='SELECT * FROM persona'
	#Persona_D.eliminar(dato)
	datoz=Persona_D.consultar()

	df=pd.DataFrame(datoz,columns=["ID","Nombre","Telefono","Email","Estado","Tipo"])
	print(df)
	#print("ID   Nombre  Telefono    Email            Estado      Tipo")
	#for i in datoz:
	#print(f"{i[0]}\t {i[1]}\t {i[2]}\t {i[3]}\t{i[4]}\t{i[5]}")

	ELIMINAR='DELETE FROM persona WHERE id_persona=?'
	#
	MODIFICAR="UPDATE persona set nombre=? where id_persona=?"

	"""