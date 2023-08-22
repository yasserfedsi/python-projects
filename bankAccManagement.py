class BankAccount:

    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        if amount <= self.initial_balance:
            self.initial_balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.initial_balance

    def get_account_number(self):
        return self.account_number
    

def create_account():
    account_number = input("Enter your account number: ")
    initial_balance = float(input("Enter the initial balance: "))
    return BankAccount(account_number, initial_balance)

while True:
    print("===========Welcome to BankAccountManagement===========")
    print("Select one of the options: ")
    print("1. Create and manage an account")
    print("2. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            # Create an account using the create_account function
            account = create_account()

            # Deposit money
            account.deposit(float(input("Enter the deposit amount: ")))

            # Withdraw money
            account.withdraw(float(input("Enter the withdrawal amount: ")))

            # Get balance and account number
            print("Account Number:", account.get_account_number())
            print("Balance:", account.get_balance())
        elif choice == "2":
            print("Goodbye! Thank you for using BankAccountManagement.")
            break
        else:
            print("Invalid option. Please select a valid option.")
    except ValueError:
        print("Please enter a valid number.")
