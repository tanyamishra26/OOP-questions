# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details. Give the complete code for the BankAccount class.
class BankAccount:
    def __init__(self,accountNumber,name,__balance):
        self.__accountNumber=accountNumber
        self.__name=name
        self.__balance=__balance
    
    def deposit(self,amount):
        self.__balance+=amount
        
    def withdrawal(self,amount):
        self.__balance-=amount
        
    def bankFees(self):
        self.__balance-=self.__balance*0.05
        
    def display(self):
        print("Account Number : ",self.__accountNumber)
        print("Account Name : ",self.__name)
        print("Account Balance : ",self.__balance)
        
newAccount = BankAccount(2178514584, "Mandy" , 2800)

newAccount.withdrawal(700)

newAccount.deposit(1000)

newAccount.display()
    
    
