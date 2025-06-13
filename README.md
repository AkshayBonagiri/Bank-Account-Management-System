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
```
## ✅ Things I Learned

1. **Object-Oriented Programming (OOP) Concepts**
   - How to define **classes** and create **objects**.
   - Using **`__init__()`** to initialize object attributes.
   - Applying **inheritance** to extend base class features (e.g., `InterestRewardAccount` inherits from `Bankaccounts`).

2. **Method Overriding**
   - How to **override** a method in a child class to provide special behavior (5% interest on deposits).

3. **Encapsulation**
   - Grouping data (`balance`, `name`) and related functions (**Deposit**, **Withdraw**, etc.) together for better organization.
