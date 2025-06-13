# Base class for bank accounts
class Bankaccounts:
    def __init__(self, InitalAmount, Accountname):
        # Initialize account with balance and name
        self.balance = InitalAmount
        self.name = Accountname
        print(f"\nBank Account Created!\nAccount Name: {self.name}\nBalance: {self.balance}$")

    def getBalance(self):
        # Display and return current balance
        print("Getting Balance...")
        print(f"\nBalance: {self.balance}$")
        return self.balance

    def Deposit(self, DepositAmount):
        # Add money to the account
        print("Depositing...")
        self.balance += DepositAmount
        print(f"\nAccount Name: {self.name}\nAmount deposited: {DepositAmount}$\nBalance: {self.balance}$")
        return self.balance

    def Withdraw(self, WithdrawAmount):
        # Withdraw money if sufficient balance is available
        print("Withdrawing...")
        if WithdrawAmount > self.balance:
            print(f"\nSorry! Your account only has {self.balance}$")
        else:
            self.balance -= WithdrawAmount
            print(f"\nAccount Name: {self.name}\nAmount withdrawn: {WithdrawAmount}$\nBalance: {self.balance}$")

    def Transfer(self, TransferAmount, ToAccount):
        # Transfer money to another account if balance allows
        print("Transferring...")
        if TransferAmount > self.balance:
            print(f"\nSorry! Your account only has {self.balance}$\nYou cannot transfer {TransferAmount}$ to {ToAccount.name}")
        else:
            self.Withdraw(TransferAmount)
            ToAccount.Deposit(TransferAmount)
            print(f"\nAmount in {self.name}: {self.getBalance()}$\nAmount in {ToAccount.name}: {ToAccount.getBalance()}$")


# Child class that adds 5% bonus on deposits
class InterestRewardAccount(Bankaccounts):
    def Deposit(self, Amount):
        # Deposit money with a 5% bonus interest
        self.balance += (1.05 * Amount)
        print(f"Balance: {self.balance}")
        print("Deposit completed!")
