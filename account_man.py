from sqliteMan import Manager
from account import Account

class AccountManager(object):
	def __init__(self):
		self.man = Manager() 
		self.query = ""
	def _table_clients(self):
		columns = []
		columns.append(self.)
