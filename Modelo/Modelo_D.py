import sys 
sys.path.append("../Controlador")
from Color import Color
from Color_D import Color_D 
from Modelo import Modelo
from Marca import Marca
from conexion import Conexion
from funciones import * 
import pandas as pd
SELECCIONAR2='SELECT * FROM modelo'
ELIMINAR2='DELETE FROM modelo WHERE id_modelo=?'
INSERTAR2='INSERT INTO  modelo(id_modelo,modelo) VALUES(?,?)'
MODIFICAR2="UPDATE modelo set modelo=? where id_modelo=?"
SELECCIONAR3='SELECT * FROM marca'
ELIMINAR3='DELETE FROM marca WHERE id_marca=?'
INSERTAR3='INSERT INTO  marca(id_marca,marca) VALUES(?,?)'
MODIFICAR3="UPDATE marca set marca=? where id_marca=?"
class Modelo_D(Color_D):
	pass
class Marca_D(Color_D):
	pass
if __name__=='__main__':
	marc=Marca(12,"Mercedes")
	dato=(marc.id_marca,marc.marca)
	Marca_D.insertar(INSERTAR3,dato)
