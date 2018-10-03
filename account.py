
class Account(object):
	def __init__(self,uname,balance):
		self._accountHolder = uname
		try:
			self._amount = float(balance)
		except:
			self._amount = float(0)
	
	def depositAmount(self,deposited):
		self._amount += float(deposited)
		return self._amount
		
	def withdraw(self,amount):
		self._amount -= float(amount)
		return self._amount
	
	def getAccountHolder(self):
		return self._accountHolder
	def getAmount(self):
		return self._amount
