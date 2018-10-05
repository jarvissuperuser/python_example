# test File
from os import system

from sqliteMan import Manager

man = Manager()
cols =["name","surname"]

vals = ["timothy","mugadza"]
table = "test_table"
qry = man.select_(cols,table)
print(qry)
qry = man.insert(table,cols,vals)
crsr = man.sql_query(qry)
#crsr.commit()
print(qry)
qry = man.delete(table,cols[1],vals[1])
print(qry)
qry = man.update(table,cols,vals,"target","int_id")
print(qry)
columns = []
columns.append(man.column_().int_().primary_().build_())
columns.append(man.column_("name").string_().build_())
columns.append(man.column_("surname").string_().build_())
qry = man.createTable(table,",".join(columns))
print(qry)
crsr = man.sql_query(qry)
#crsr.commit()
