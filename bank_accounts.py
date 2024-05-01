# create class for bank accout
class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, acctName, initialBalance):
        self.name = acctName
        self.balance = initialBalance
        print(f"\nAccount for {self.name} has been created with £{self.balance:.2f} balance")
        #format balance to 2 decimal places

    def get_balance(self):
        print (f"\n{self.name} has £{self.balance:.2f} in the account")
        #format balance to 2 decimal places

    def deposit(self, amount):
        self.balance += amount
        print (f"\nDeposit complet.")
        self.get_balance()
        return self.balance

    #check to see if its a valid withdrawal
    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nInsufficient funds. Account for {self.name} only has a blance of £{self.balance:.2f} in the account")
        
    # check to see if its a valid recipient
    def check_recipient(self, recipient):
        if recipient != self.name:
            return
        else:
            raise BalanceException(f"\nYou cannot transfer money to this account {self.name} as it doesnt exist.")

    def withdraw(self, amount):
        try:
            #check if withdrawal is valid
            self.check_withdrawal(amount)
            #if valid, withdraw amount
            self.balance -= amount
            #print balance  
            print (f"\nWithdrawal complet.")
            #format balance to 2 decimal places
            self.get_balance()
        except BalanceException as e:
            print(f"\nWithdraw interupted {e}")
        
    # transfer method
    def transfer(self, amount, recipient):
        try:
            print (f"\n**************\n\nBeginning Transfer ...📈")
            #check if withdrawal is valid
            self.check_withdrawal(amount)
            # if valid withdraw
            self.withdraw(amount)
            #check if recipient is valid
            self.check_recipient(recipient)
            #if valid, deposit amount
            recipient.deposit(amount)
            #print transfer complete  
            print (f"\nTransfer complet! ✅\n\n**************\n")
        except BalanceException as e:
            print(f"\nTransfer interupted!! ❌ {e}")


    def __str__(self):
        return f"{self.name} has {self.balance} in the account"
    
class IntrestRewards(BankAccount):
    # add extra 5% intrest to the account
    def deposit(self, amount):
        self.balance += (amount*1.05)
        print (f"\nDeposit complet.")
        self.get_balance()

# create a savings account class , inheriting from intrest rewards
class SavingsAccount(IntrestRewards):
    # Savings account will have another properrty to the class called fee
    def __init__(self, acctName, initialBalance):
        super().__init__(acctName, initialBalance)
        # fee for every withdrawal
        self.fee = 0.20
    
    def withdraw(self, amount):
        try:
            #check if withdrawal is valid , include fee
            self.check_withdrawal(amount + self.fee)
            #if valid, withdraw amount and fee
            self.balance -= (amount + self.fee)
            #print balance  
            print (f"\nWithdrawal complet.")
            #format balance to 2 decimal places
            self.get_balance()
            # call the balance method
        except BalanceException as e:
            print(f"\nWithdraw interupted {e}")