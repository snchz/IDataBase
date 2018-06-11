# IDataBase
Interfaz de base de datos para sqlite3.

#Ejemplo de uso
from IDataBase import DataBase
db=DataBase("datos.db")db.modify("CREATE TABLE IF NOT EXISTS TablaEjemplo (asunto TEXT, orden INTEGER);")
db.modify("INSERT INTO TablaEjemplo VALUES('Ejemplo B',2);")
db.modify("INSERT INTO TablaEjemplo VALUES('Ejemplo A',1);")
db.modify("INSERT INTO TablaEjemplo VALUES('Ejemplo C',3);")
db.select("SELECT * FROM TablaEjemplo ORDER BY orden DESC;",1)
