from querybuilder import QueryBuilder

class Ctable(object):
	def __init__(self):
		self._q = QueryBuilder()
		self._c = ["firstname","surname","idnumber"]
		self._t = "clients"
		
	def _columns(self):
		columns = []
		columns.append(self._q.column_().int_().primary_().auto_increment().build_())
		columns.append(self._q.column_(self._c[0]).string_().build_())
		columns.append(self._q.column_(self._c[1]).string_().build_())
		columns.append(self._q.column_(self._c[2]).string_(15).unique().not_null().build_())
		return columns
		
	def	table_create(self):
		cols = self._columns();
		return self._q.createTable(self._t,",".join(cols))
		
