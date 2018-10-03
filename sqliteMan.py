from sqlite3 import connect,Connection
sql = connect("./sdb.db")
connection = sql
class Manager(object):
	def __init__(self,f_path):
		self._conn = connect("./sdb.db")
	def createTable(self):
		return "table";
	def select(_):
		return "table";
	def delete(_):
		return "table";
	def insert(_):
		return "table";
	def update(_):
		return "table";
