import account as Ac

Acc = Ac.Account

class Operation(object):

	def addAccount(self):
		userName = input(self._msg("Please New AccountHolder :",'r'))
		initialAmount = input(self._msg("Please Enter Amount :",'r'))
		print(self._msg("\t|\tAccount Added\t|"))
		return Acc(userName,initialAmount)
		
	def findAccount(self,accounts):
		userName = input(self._msg("Please Enter Account Identifier : ",'y'))
		for account in accounts:
			if account.getAccountHolder()==userName:
				print(self._msg("\t|\tAccount Selected\t|",'g'))
				return account
		print(self._msg("\tAccount Not Found",'r'))
		
	def printOptions(self):
		print(self._msg("\tOption 1 : Add Account ",'y'))
		print(self._msg("\tOption 2 : Search Account",'y'))
		print(self._msg("\tOption 3 : Deposit Account",'y'))
		print(self._msg("\tOption 4 : Balance Check",'y'))
		print(self._msg("\tOption clear : clear screen",'d'))
		print(self._msg("\tOption q : Quit and exit",'b'))
				
	
		

	def doOp(self,opt,accounts=[],deposit=0):
		if (opt == '1'):
			accounts.append(self.addAccount())
		elif(opt == '2'):
			a = self.findAccount(accounts)
			self._loadedAccount = a;
			#print(self._msg("\t|\tAccount Selected\t|",'g'))
		elif(opt == '3'):
			self.safeDeposit()
		elif(opt == '4'):
			self.safeBalCheck()
			
	def getAccount(self,acc):
		return "\t|\tAccount {} => {}\t|".format(acc.getAccountHolder(),acc.getAmount())

	def depositAmount(_,acc):
		deposited = input(_._msg("Please Enter Deposited Amount","r"))
		acc.depositAmount(deposited)
		
	def safeDeposit(self):
		try:
			acc = self._loadedAccount
		except:
			print(self._msg("\t|\tNo Account Selected\t|",'r'))
		else:
			self.depositAmount(acc);
			del self._loadedAccount
			print(self._msg("\t|\tSuccess=>Account Deselected\t|",'g'))

	def safeBalCheck(self):
		try:
			acc = self._loadedAccount
		except:
			print(self._msg("\t|\tNo Account Selected\t|",'r'))
		else:
			print(self.getAccount(acc));
			print(self._msg("\t|\tSuccess=>Account Deselected\t|",'g'))
			
	def _green(_,msg):
		return "\x1b[32m".__add__(msg)
	
	def _red(_,msg):
		return "\x1b[31m".__add__(msg)
	
	def _blue(_,msg):
		return "\x1b[35m".__add__(msg)
		
	def _yel(_,msg):
		return "\x1b[33m".__add__(msg)
		
	def _msg(self,msg,c='d'):
		return {
		'd': msg,'g': self._green(msg),
		'r': self._red(msg),
		'b': self._blue(msg),
		'y': self._yel(msg),
		}[c].__add__("\x1b[0m")
	
