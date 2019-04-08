

class QueryBuilder(object):
	def build_(self):
		val = self.val
		self.val = 0
		return val

	def createTable(self,name_table,columns):
		query = "CREATE TABLE IF NOT EXISTS ".__add__(name_table)
		query = query.__add__(" (");
		query = query.__add__(columns);
		return query.__add__(")")
		
	def column_(self,name="id"):
		self.val = name
		return self
	def default(self,default_ = '0'):
		self.val = self.val.__add__(" DEFAULT ");
		self.val = self.val.__add__(str(default_));
		RETU
		
	def not_null(self):
		self.val = self.val.__add__(" NOT NULL ")
		return self 
	def type(self):
		return self
	def int_(self):
		self.val = self.val.__add__(" INTEGER ")
		return self
	def string_(self,size_=0):
		if (size_==0):
			self.val = self.val.__add__(" TEXT ")
		else:
			self.val = self.val.__add__(" VARCHAR(")
			self.val = self.val.__add__(str(size_))
			self.val = self.val.__add__(")")
		return self
	def real_(self,):
		self.val = self.val.__add__(" REAL ")
		return self
	def auto_increment(self):
		self.val = self.val.__add__(" AUTOINCREMENT ")
		return self				
	def primary_(self):
		self.val = self.val.__add__("PRIMARY KEY")
		return self
	def unique(self):
		self.val = self.val.__add__(" UNIQUE ")
		return self
		
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
		valstr = self._column_expand(vals,1)
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
	
