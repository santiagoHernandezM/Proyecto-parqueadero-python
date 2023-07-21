import sys 
sys.path.append("../Controlador")
from Automovil import Automovil 
from Persona_D import Persona_D
from conexion import Conexion
import pandas as pd

class Automovil_D(Persona_D):
	pass	

if __name__=='__main__':


	auto=Automovil(8,"QWE124",1,2,23,1,100)
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

	ELIMINAR='DELETE FROM auto WHERE id_automovil=?'
	MODIFICAR="UPDATE auto set marca=? where placa=?"
	