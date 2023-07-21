import sqlite3
""" 
class Conexion:
	conexion=None
	cursor=None
	@classmethod
	def ObtenerConexion(self):
		self.conexion=sqlite3.connect('PARQUEADERO.db')
		return self.conexion
	@classmethod
	def ObtenerCursor(self):
		self.cursor=self.ObtenerConexion().cursor()
		return self.cursor



"""

import sqlite3
class Conexion:
	#@classmethod
	def ObtenerConexion():
		conexion=sqlite3.connect('PARQUEADERO.db')
		return conexion
	#def ObtenerCursor(conexion):
	#	cursor=conexion.cursor()
	#	return cursor
