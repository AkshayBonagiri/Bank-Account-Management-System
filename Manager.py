from Bank_accounts import *

# Sample usage of the Bank Account Management System

# Create a regular bank account
acc1 = Bankaccounts(500, "Akshay")

# Create an interest reward account
acc2 = InterestRewardAccount(1000, "Savings Account")

# Check initial balances
acc1.getBalance()
acc2.getBalance()

# Deposit money into both accounts
acc1.Deposit(200)
acc2.Deposit(300)

# Withdraw money from the regular account
acc1.Withdraw(100)

# Attempt to withdraw more than the balance to test error handling
acc1.Withdraw(1000)

# Transfer money from regular account to interest account
acc1.Transfer(300, acc2)

# Final balances
acc1.getBalance()
acc2.getBalance()

