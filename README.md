# 💰 Bank Account Management System

A Python-based **Object-Oriented** banking simulation that allows users to create accounts, deposit funds, withdraw money, and transfer balances between accounts. It also features an **Interest Reward Account** that gives a 5% bonus on deposits.

---

## 🚀 Features

- 🏦 Create and manage multiple bank accounts
- 💵 Deposit money into an account
- 🏧 Withdraw money with balance validation
- 🔄 Transfer funds between two accounts
- 🎁 InterestRewardAccount → Adds 5% bonus to every deposit

---

## 📂 How to Use

1. Clone or download the code.
2. Run the Python script.
3. Create account objects and call methods like:
   - `.getBalance()`
   - `.Deposit(amount)`
   - `.Withdraw(amount)`
   - `.Transfer(amount, to_account)`

---

## 📌 Example Usage

```python
acc1 = Bankaccounts(500, "John")
acc2 = InterestRewardAccount(1000, "Jane")

acc1.Deposit(100)
acc2.Deposit(200)

acc1.Withdraw(50)
acc1.Transfer(200, acc2)
---

## Things I Learned
✅ Object-Oriented Programming (OOP) Concepts

Defining classes and creating objects

Using constructors (__init__()) to initialize data

Applying inheritance to extend functionality (InterestRewardAccount)

✅ Method Overriding

Overriding parent class methods in child classes to customize behavior (e.g., adding 5% interest on deposits)

✅ Encapsulation

Keeping data (balance, name) and behavior (Deposit, Withdraw) together inside a class
