# test File
from os import system
from accountstable import Atable
from transactionstable import Ttable
from clienttable import Ctable
from sqliteMan import Manager

man = Manager()
cols =["name","surname"]

vals = ["timothy","mugadza"]
table = "test_table"
qry = man.select_(cols,table)
print(qry)
qry = man.insert(table,cols,vals)
#crsr = man.sql_query(qry)
#crsr.commit()
print(qry)
qry = man.delete(table,cols[1],vals[1])
print(qry)
qry = man.update(table,cols,vals,"target","int_id")
print(qry)
columns = []
columns.append(man.column_().int_().primary_().auto_increment().build_())
columns.append(man.column_("name").string_().build_())
columns.append(man.column_("surname").string_().build_())
qry = man.createTable(table,",".join(columns))
#qry += "; UPDATE sqlite_sequence SET seq = 1"
print(qry)
#crsr = man.sql_query(qry)
#crsr.commit()


tables = []
tables.append(Atable().table_create())
tables.append(Ctable().table_create())
tables.append(Ttable().table_create())

for i in tables:
	print(i)
	man.sql_query(i)
