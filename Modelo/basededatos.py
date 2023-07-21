import sqlite3
conn = sqlite3.connect("PARQUEADERO.db")
cursor = conn.cursor()
sql = """
DROP TABLE IF EXISTS persona;
DROP TABLE IF EXISTS auto;
DROP TABLE IF EXISTS apartamento;
DROP TABLE IF EXISTS parqueadero;
DROP TABLE IF EXISTS celda;
DROP TABLE IF EXISTS historial;
DROP TABLE IF EXISTS camaras;
DROP TABLE IF EXISTS marca;
DROP TABLE IF EXISTS modelo;
DROP TABLE IF EXISTS color;

CREATE TABLE persona (
id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
nombre VARCHAR(35) NOT NULL,
telefono VARCHAR(35) NOT NULL,
email VARCHAR(35) NOT NULL,
estado INTEGER NOT NULL,
tipo VARCHAR(35) NOT NULL
);

CREATE TABLE auto (
id_automovil INTEGER PRIMARY KEY AUTOINCREMENT,
placa VARCHAR NOT NULL,
id_marca INTEGER NOT NULL,
id_modelo INTEGER NOT NULL,
id_color INTEGER NOT NULL,
estado INTEGER,
id_persona INTEGER,
FOREIGN KEY(id_marca) REFERENCES marca(id_marca),
FOREIGN KEY(id_modelo) REFERENCES modelo(id_modelo),
FOREIGN KEY(id_color) REFERENCES marca(id_color),
FOREIGN KEY(id_persona) REFERENCES persona(id_persona));

CREATE TABLE marca (
id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
marca VARCHAR(35) NOT NULL);

CREATE TABLE modelo (
id_modelo INTEGER PRIMARY KEY AUTOINCREMENT,
modelo VARCHAR(35) NOT NULL);

CREATE TABLE color (
id_color INTEGER PRIMARY KEY AUTOINCREMENT,
color VARCHAR(35) NOT NULL);


CREATE TABLE apartamento (
id_apartamento INTEGER PRIMARY KEY AUTOINCREMENT,
bloque VARCHAR(35) NOT NULL,
numero INTEGER,
id_persona INTEGER NOT NULL,
FOREIGN KEY(id_persona) REFERENCES persona(id_persona));

CREATE TABLE parqueadero (
id_parqueadero INTEGER PRIMARY KEY AUTOINCREMENT,
numero INTEGER NOT NULL,
totalceldas INTEGER);


CREATE TABLE celda (
id_celda INTEGER PRIMARY KEY AUTOINCREMENT,
id_parqueadero INTEGER NOT NULL,
id_apartamento INTEGER NOT NULL,
numerocelda INTEGER NOT NULL,
FOREIGN KEY(id_parqueadero) REFERENCES parqueadero(id_parqueadero),
FOREIGN KEY(id_apartamento) REFERENCES apartamento(id_apartamento));

CREATE TABLE camaras (
id_camara INTEGER PRIMARY KEY AUTOINCREMENT,
id_parqueadero INTEGER NOT NULL,
numero INTEGER NOT NULL,
area INTEGER NOT NULL,
longitud INTEGER NOT NULL,
FOREIGN KEY(id_parqueadero) REFERENCES parqueadero(id_parqueadero));

CREATE TABLE historial (
id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
id_automovil INTEGER,
id_camara INTEGER,
fechahora DATETIME,
FOREIGN KEY(id_automovil) REFERENCES auto(id_automovil),
FOREIGN KEY(id_camara) REFERENCES camaras(id_camara));
"""

try:
    cursor.executescript(sql)
    print('La base de datos fue creada')
except sqlite3.Error as e:
    print('Ha ocurrido un error', e.args)
conn.close()