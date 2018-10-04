# test File
from os import system

from sqliteMan import Manager

man = Manager()
cols =["test","got","fast"]
vals =cols[::-1]
table = "table"
qry = man.select_(cols,table)
print(qry)
qry = man.insert(table,cols,vals)
print(qry)
qry = man.delete(table,cols[2],vals[1])
print(qry)
qry = man.update(table,cols,vals,"target","int_id")
print(qry)
columns = []
columns.append(man.column_().int_().primary_().build_())
columns.append(man.column_("name").string_().build_())
columns.append(man.column_("surname").string_().build_())
qry = man.createTable(table,",".join(columns))
print(qry)
