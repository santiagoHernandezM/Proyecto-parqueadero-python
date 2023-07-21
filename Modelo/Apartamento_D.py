import sys 
sys.path.append("../Controlador")
from Apartamento import Apartamento
from Persona_D import Persona_D
from Parqueadero import Parqueadero
from Automovil import Automovil
from Camaras import Camaras
from Celda import Celda
from Color import Color
from Historial import Historial
from Modelo import Modelo
from conexion import Conexion
import pandas as pd
class Apartamento_D(Persona_D):
	pass
class Parqueadero_D(Persona_D):
	pass
class Automovil_D(Persona_D):
	pass
class Camaras_D(Persona_D):
	pass
class Celda_D(Persona_D):
	pass
class Color_D(Persona_D):
	pass
class Historial_D(Persona_D):
	pass
class Modelo_D(Persona_D):
	pass

if __name__=='__main__':
	
	#"(Parqueadero)"
	"""
	parqueadero=Parqueadero(4,5,96)
	INSERTAR='INSERT INTO  parqueadero(id_parqueadero,numero,totalceldas) VALUES(?,?,?)'
	dato=[parqueadero.id_parqueadero,parqueadero.numero,parqueadero.totalceldas]
	Parqueadero_D.insertar(INSERTAR,dato)
	SELECCIONAR='SELECT * FROM Parqueadero'
	datoz=Parqueadero_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["ID Parqueadero","Numero de Celdas","Total de Celdas"])
	print(df)
	#ELIMINAR='DELETE FROM Parqueadero WHERE id_parqueadero=?'
	#MODIFICAR="UPDATE Parqueadero set totalceldas=? where id_parqueadero=?"
	"""

	#"(Apartamento)"
	"""
	apartamento=Apartamento(220,5,100,1)
	INSERTAR='INSERT INTO  apartamento(id_apartamento,Bloque,numero,id_persona) VALUES(?,?,?,?)'
	dato=[apartamento.id_apartamento,apartamento.bloque,apartamento.numero,apartamento.id_persona]
	Apartamento_D.insertar(INSERTAR,dato)
	SELECCIONAR='SELECT * FROM apartamento'
	datoz=Apartamento_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["ID","Bloque","Numero","Id_persona"])
	print(df)
	#dato=(2,205)
	#Apartamento_D.modificar(dato)
	#dato=(210,)
	#Apartamento_D.eliminar(dato)
	#Persona_D.eliminar(dato)
	#ELIMINAR='DELETE FROM apartamento WHERE id_apartamento=?'
	#MODIFICAR="UPDATE apartamento set bloque=? where id_apartamento=?"
"""

	#"(Automovil)"
	"""
	auto=Automovil(9,"QWE124",1,2,23,1,100)
	INSERTAR='INSERT INTO  auto(id_automovil,placa,id_marca,id_modelo,id_color,estado,id_persona) VALUES(?,?,?,?,?,?,?)'
	dato=[auto.id_automovil,auto.placa,auto.id_marca,auto.id_modelo,auto.id_color,auto.estado,auto.id_persona]
	Automovil_D.insertar(INSERTAR,dato)
	
	#dato=(2,)
	#Persona_D.modificar(dato)
	#Automovil_D.eliminar(dato)
	#dato=(201,)

	#Persona_D.eliminar(dato)
	SELECCIONAR='SELECT * FROM auto'
	datoz=Automovil_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["id_automovil","Placa","Marca","Modelo","Color","Estado","id_persona"])
	print(df)

	#ELIMINAR='DELETE FROM auto WHERE id_automovil=?'
	#MODIFICAR="UPDATE auto set marca=? where placa=?"
	"""

	#"(camara)"
	"""
	Camaras=Camaras(2,5,9,93,56)
	SELECCIONAR='SELECT * FROM Camaras'
	INSERTAR='INSERT INTO  camaras(id_camara,id_parqueadero,numero,area,longitud) VALUES(?,?,?,?,?)'
	dato=[Camaras.id_camara,Camaras.id_parqueadero,Camaras.numero,Camaras.area,Camaras.longitud]
	Camaras_D.insertar(INSERTAR,dato)
	datoz=Camaras_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["ID Camaras","ID Parqueadero","Numero","Area","Longitud"])
	print(df)

	#dato=(100,50,25,1)
	#Camaras_D.MODIFICAR(dato)

	#dato=(2,)
	#Camaras_D.ELIMINAR(dato)
    
	#ELIMINAR='DELETE FROM Camaras WHERE id_camara=?'
	#INSERTAR='INSERT INTO  Camaras(id_camara,id_parqueadero,numero,area,longitud) VALUES(?,?,?,?,?)'
	#MODIFICAR="UPDATE Camaras set numero=?, area=?, longitud=? where id_camara=?"


	