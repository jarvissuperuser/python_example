from querybuilder import QueryBuilder

class Ttable(object):
	def __init__(self):
		self._q = QueryBuilder()
		self._c = ["reference","creference","account","transactionstatus"
		,"amount"]
		self._t = "transactions"
		
	def _columns(self):
		columns = []
		columns.append(self._q.column_().int_().primary_().auto_increment().build_())
		columns.append(self._q.column_(self._c[0]).string_().build_())
		columns.append(self._q.column_(self._c[1]).string_().build_())
		columns.append(self._q.column_(self._c[2]).real_().build_())
		columns.append(self._q.column_(self._c[3]).string_(2).build_())
		columns.append(self._q.column_(self._c[4]).real_().not_null().build_())
		return columns
		
	def	table_create(self):
		cols = self._columns();
		return self._q.createTable(self._t,",".join(cols))
