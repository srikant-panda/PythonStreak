class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        # self.balance = balance  # This is a public, anyone can access it
        self.__balance = balance  #Now this is private , now it won't be accessed directly

    def deposite(self,amount):
            self.__balance = self.__balance+amount
            print(f'Deposited {amount} , New balance {self.__balance}')
        
    def getBalance(self):
            return self.__balance
    

account_holder1=BankAccount(453628361,2000)

account_holder1.deposite(5000)
print(account_holder1.getBalance())
# print(account_holder1.__balance)   # This will give attribute error bcz we seeted it private. But
print(account_holder1._BankAccount__balance)  #To access __balence we can write this.