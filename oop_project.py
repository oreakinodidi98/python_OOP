# import all classes in bank_accounts
from bank_accounts import *

# create a new instance of bank account

Dave = BankAccount("Dave", 2000)
Ore = BankAccount("Ore", 10000)

#call the get_balance method
Ore.get_balance()
Dave.get_balance()

#call the deposit method
Ore.deposit(1000)
Dave.deposit(5000)

#call the withdraw method
Ore.withdraw(50000)
Dave.withdraw(5000)

#call the transfer method
Ore.transfer(5000, Dave)

# new intrest rewards account
Jim = IntrestRewards("Jim", 1000)
Jim.get_balance()
Jim.deposit(100) # jim should get 5% intrest on this deposit so he should have £1105 in total
Jim.transfer(1000, Ore) 

# new savings account
Tom = SavingsAccount("Tom", 5000)
Tom.get_balance()
Tom.deposit(100)
Tom.withdraw(10000)
Tom.transfer(1000, Ore)
Tom.withdraw(100)