from sqlite3 import connect,Connection
from querybuilder import QueryBuilder

class Manager(QueryBuilder):
	def __init__(self,f_path="./sdb.db"):
		try:
			self._conn = connect(f_path)
		except:
			self._conn = 0
			print("No DB connection")
	
	
	def sql_query(self,sql_):
		cursor = self._conn.cursor()
		return cursor.execute(sql_)
	
	def getConnection(self):
		return self._conn
		
