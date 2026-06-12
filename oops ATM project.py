from datetime import datetime


class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance
        self.transactions = []
        self.attempts = 3

    def withdraw(self):
        amount = int(input("Enter Amount: "))

        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(
                f"{datetime.now()} - Withdraw ₹{amount}"
            )
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def deposit(self):
        amount = int(input("Enter Amount: "))
        self.balance += amount

        self.transactions.append(
            f"{datetime.now()} - Deposit ₹{amount}"
        )

        print("Amount Deposited Successfully")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def mini_statement(self):
        print("\n----- MINI STATEMENT -----")

        if len(self.transactions) == 0:
            print("No Transactions Found")
        else:
            for transaction in self.transactions:
                print(transaction)

    def change_pin(self):
        old_pin = input("Enter Old PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter New PIN: ")
            self.pin = new_pin
            print("PIN Changed Successfully")
        else:
            print("Wrong PIN")

    def fast_cash(self):
        print("1. ₹500")
        print("2. ₹1000")
        print("3. ₹2000")
        print("4. ₹5000")

        choice = int(input("Choose Option: "))

        if choice == 1:
            amount = 500
        elif choice == 2:
            amount = 1000
        elif choice == 3:
            amount = 2000
        elif choice == 4:
            amount = 5000
        else:
            print("Invalid Option")
            return

        if amount <= self.balance:
            self.balance -= amount

            self.transactions.append(
                f"{datetime.now()} - Fast Cash ₹{amount}"
            )

            print("Please Collect Your Cash")
        else:
            print("Insufficient Balance")

    def transfer_money(self):
        account = input("Enter Account Number: ")
        amount = int(input("Enter Amount: "))

        if amount <= self.balance:
            self.balance -= amount

            self.transactions.append(
                f"{datetime.now()} - Transfer ₹{amount} to {account}"
            )

            print("Transfer Successful")
        else:
            print("Insufficient Balance")

    def login(self):
        while self.attempts > 0:
            entered_pin = input("Enter PIN: ")

            if entered_pin == self.pin:
                print("Login Successful")
                return True
            else:
                self.attempts -= 1
                print("Wrong PIN")
                print("Attempts Left:", self.attempts)

        print("Card Blocked")
        return False

    def menu(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Mini Statement")
            print("5. Change PIN")
            print("6. Fast Cash")
            print("7. Transfer Money")
            print("8. Exit")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.withdraw()

            elif choice == 2:
                self.deposit()

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                self.mini_statement()

            elif choice == 5:
                self.change_pin()

            elif choice == 6:
                self.fast_cash()

            elif choice == 7:
                self.transfer_money()

            elif choice == 8:
                print("Thank You For Using ATM")
                break

            else:
                print("Invalid Choice")


# Main Program
atm = ATM("1234", 10000)

if atm.login():
    atm.menu()
