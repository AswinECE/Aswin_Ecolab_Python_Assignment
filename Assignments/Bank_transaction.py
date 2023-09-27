class Bank_account:
    def __init__(self,account_number,name,password,balance,interest):  
        self.account_number=account_number
        self.name=name
        self.password=password
        self.balance=balance
        self.interest= interest

        print("WELCOME\t,", name)
    
    def info(self):
        print("Account balance :",self.balance)

    def deposit(self,amount):
        if(amount>0):
            print("Deposit amount Rs. ",amount)
            total_balance=self.balance + amount
            print("Account balance :" ,total_balance)
        else:
            print("Invalid entry \n Transaction failed")

    def withdraw(self,password,amount):
        if(password == self.password):
            if(amount>0):
                if(amount<=self.balance):
                    new_balance= self.balance - amount
                    print("Withdrawn Rs. ", amount)
                    print("Current bank balance :",new_balance)
                else:
                    print("Transaction failed \nInsufficient fund")
            else:
                print("Enter a valid amount")
        else:
            print("Incorrect password \n Try again")

    def credit_interest(self):
        new_interest=self.balance+(self.balance * self.interest /1200)
        print("Credit rate:",new_interest)

object=Bank_account(36104304281,"ASWIN S",2228,25000,6)
object.info()
#object.deposit(50000)
object.withdraw(2228,5000)
object.credit_interest()