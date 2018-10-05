# udemy
# import Account as Acc
from operation import Operation
from os import system 
accounts = []
op = Operation()
#print(Op)
if __name__ == "__main__":
	while(True):
		op.printOptions()
		options='0'
		options = input("Selection : ")
		if options=="q":
			break
		elif (options!="clear"):
			system("clear")
			op.doOp(options,accounts)
		else:
			system("clear")

