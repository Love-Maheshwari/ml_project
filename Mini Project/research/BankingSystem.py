#Parent class :User
#Child class : Bank
#Stores the details of the account balance
#Allows for the deposit, withdraw and view_balance

class User:
    """
    A class to represent a user.
    Attributes
    ----------
    name : str
        The name of the user.
    account_number : float
        The account_number of the user.
    balance : float
        Total Balance of the user.
    Methods
    -------
    show_details():
        Prints the details of the user.
    """
    def __init__(self,name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
               
    def show_details(self):
        print(f"Name: {self.name}", "\n" f"account_number: {self.account_number}", "\n" f"Total balance is : {self.balance}")



#Child class
class Bank(User):
    def __init__(self, name, account_number, balance):
        super().__init__(name, account_number, balance)   

    def deposit(self):
        amount = float(input("enter the non negative amount"))
        self.balance += amount
        print(f"the amount deposited is : {amount} and current balance ios :{self.balance}")
    
    def withdraw(self):
        
        amount = float(input("How much do you want to withdraw"))
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} Withdraw {amount} $. Current balance is: {self.balance}")
        else:
            print("You don't have enough funds to withdraw.")


user1 = Bank("A", 123, 1000)
user2 = Bank("B", 1234, 2000)

user1.show_details()
user1.deposit()
user1.withdraw()    