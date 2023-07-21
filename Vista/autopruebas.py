import sys 
sys.path.append("../Controlador")
sys.path.append("../Modelo")
from Automovil import Automovil 
from Automovil_D import Automovil_D
from conexion import Conexion
import pandas as pd
def main():
	pass
if __name__ == '__main__':
	#main()
	#INSERTAR='INSERT INTO  auto (id_automovil,placa,id_marca,id_modelo,id_color,estado,id_persona) VALUES(?,?,?,?,?,?,?)'
	auto=Automovil(9,"AKL451",1,2,23,1,220)
	dato=[auto.id_automovil,auto.placa,auto.id_marca,auto.id_modelo,auto.id_color,auto.estado,auto.id_persona]
	Automovil_D.insertar(dato)
