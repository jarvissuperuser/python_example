from querybuilder import QueryBuilder

class Atable(object):
	def __init__(self):
		self._q = QueryBuilder()
		self._c = ["accountnumber","clientid","accounttype","amount"]
		self._t = "accounts"
		
	def _columns(self):
		columns = []
		columns.append(self._q.column_().int_().primary_().auto_increment().build_())
		columns.append(self._q.column_(self._c[0]).int_().unique().build_())
		columns.append(self._q.column_(self._c[1]).int_().build_())
		columns.append(self._q.column_(self._c[2]).string_().not_null().build_())
		columns.append(self._q.column_(self._c[3]).real_().not_null().build_())
		return columns
		
	def	table_create(self):
		cols = self._columns();
		return self._q.createTable(self._t,",".join(cols))
