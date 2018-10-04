from sqlite3 import connect,Connection

class Manager(object):
	def __init__(self,f_path="./sdb.db"):
		try:
			self._conn = connect(f_path)
		except:
			self._conn = 0
			print("No DB connection")

	def createTable(self):
		return "table"
		
	def select_(self,selection=['*'],table="",limiter="1=1"):
		str_col = self._column_expand(selection)
		query = "SELECT ".__add__(str_col)
		query = query.__add__(" FROM ")
		query = query.__add__(table)
		if (limiter!="1=1"):
			query.__add__(" WHERE ")
			query.__add__(limiter)
		return query
		
	def delete(self,table,target,id_):
		query = "DELETE FROM ".__add__(table)
		query = query.__add__(" WHERE ")
		query = query.__add__(target)
		query = query.__add__("=")
		query = query.__add__(id_)
		return query
		
	def insert(self,table,cols,vals):
		colstr = self._column_expand(cols)
		valstr = self._column_expand(vals)
		query = "INSERT INTO ".__add__(table)
		query = query.__add__(" (")
		query = query.__add__(colstr)
		query = query.__add__(") VALUES (")
		query = query.__add__(valstr)
		query = query.__add__(")")
		return query
		
	def update(self,table,cols,vals,target,id_):
		cvstr = self._col_val_str(cols,vals) 
		query = "UPDATE ".__add__(table)
		query = query.__add__(" SET ")
		query = query.__add__(cvstr)
		query = query.__add__(" WHERE ")
		query = query.__add__(target)
		query = query.__add__("=")
		query = query.__add__(id_)
		return query
	
	def _col_val_str(self,cols,vals):
		col_val = []
		for i in range(0,len(cols)):
			col_val.append(cols[i] + "=" + vals[i])
		cvstr = ",".join(col_val) 
		
		return cvstr
		
	def _column_expand(self,adjust_,mode=0):
		colstr = ""
		cols = []
		if (mode == 1):
			for col in adjust_:
				cols.append(self._ec(col,mode))
			colstr = ",".join(cols)
		else:
			colstr = ",".join(adjust_)
		return colstr
		
	def _ec(_,st,md):
		if (md == 0):
			return st
		else:
			return "'" + st + "'"
	
	def sql_query(_,sql_):
		cursor = self._conn.cursor()
		return cursor.execute();	
