import sqlite3
from datetime import datetime
import traceback

class DataBase:
	def __init__(self,sqlite_file):
		self.sqlite_file=sqlite_file
	
	#query=Sentencia CREATE, DELETE o INSERT
	def modify(self, query):
		try:
			conn=sqlite3.connect(self.sqlite_file)
			c=conn.cursor()
			c.execute(query)
			conn.commit()
			conn.close()
			return True
		except sqlite3.IntegrityError as e: #Duplicados...
			print(e)
			return -3
		except sqlite3.OperationalError as e: #La tabla ya existe
			print(e)
			return -2 
		except Exception as e:
			print(e)
			return -1
	
	#query=Sentencia SELECT a la base de datos
	#pintar= Si pintar=1 entonces pinta por pantalla el resultado
	def select(self, query, pintar):
		try:
			conn=sqlite3.connect(self.sqlite_file)
			c=conn.cursor()
			c.execute(query)
			all_rows=c.fetchall()
			conn.close()
			if pintar==1:
				for linea in all_rows:
					for columna in linea:
						print(columna,end='\t')
					print('')
			return all_rows
		except sqlite3.OperationalError as e: #La tabla ya existe
			traceback.print_exc()
			return -2
		except Exception as e:
			return -1
