# 🏦 OOP Assignment: Banking System

This Python project demonstrates core Object-Oriented Programming (OOP) principles through a simple banking system. It includes two classes—`BankAccount` and `SavingsAccount`—that simulate basic financial operations such as deposits, withdrawals, and interest calculations.

## 📦 File

- `OOP_assignment.py`: Contains all class definitions and example usage.

## 🧠 OOP Concepts Demonstrated

| Concept         | Description                                                                 |
|----------------|------------------------------------------------------------------------------|
| Encapsulation  | Private attributes (`__balance`, `__account_number`, etc.) with getter methods |
| Inheritance    | `SavingsAccount` inherits from `BankAccount`                                 |
| Polymorphism   | `display_balance()` method is overridden in `SavingsAccount`                 |
| Abstraction    | Users interact with simple methods like `deposit()` and `withdraw()`         |

## 🏗️ Class Overview

### `BankAccount`
- Attributes:
  - `account_number`
  - `account_holder`
  - `balance`
- Methods:
  - `deposit(amount)`
  - `withdraw(amount)`
  - `display_balance()`
  - Getter methods for encapsulated attributes

### `SavingsAccount` (inherits from `BankAccount`)
- Additional attribute:
  - `interest_rate`
- Additional methods:
  - `apply_interest()`
  - Overridden `display_balance()` to show interest earnings

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `OOP_assignment.py`.
4. Run the script:

```bash
python OOP_assignment.py
