import sys
import getpass

class BankAccount:
    
    def _init_(self, user_id, password, balance=0):
        self.user_id = user_id
        self.password = password
        self.balance = balance

    def deposit(self, amount):
      
        if amount > 0:
            self.balance += amount
            print(" amount deposited successfully.")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
      
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("amount withdrawn successfully.")
        else:
            print(" Insufficient balance .")

    def check_balance(self):
   
        print(" Your current balance: ₹{self.balance}")

class BankingSystem:
 
    
    def _init_(self):
        self.accounts = {}

    def create_account(self, user_id, password):
      
        if user_id in self.accounts:
            print(" User ID already exists. Try another one.")
        else:
            self.accounts[user_id] = BankAccount(user_id, password)
            print(" Account created successfully!")

    def login(self, user_id, password):
     
        if user_id in self.accounts and self.accounts[user_id].password == password:
            print(f" Login successful! Welcome, {user_id}.")
            return self.accounts[user_id]
        else:
            print(" Invalid credentials!")
            return None

def main():
   
    system = BankingSystem()

    while True:
        print("\n---  Banking System ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("Enter a new User ID: ")
            password = getpass.getpass(" Enter a password: ")
            system.create_account(user_id, password)

        elif choice == "2":
            user_id = input(" Enter User ID: ")
            password = getpass.getpass(" Enter Password: ")
            account = system.login(user_id, password)

            if account:
                while True:
                    print("\n---  Account Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    print("5. Exit System")

                    choice = input("Choose an option: ")

                    if choice== "1":
                        try:
                            amount = float(input(" Enter amount to deposit: "))
                            account.deposit(amount)
                        except ValueError:
                            print(" Please enter a valid number.")

                    elif choice == "2":
                        try:
                            amount = float(input(" Enter amount to withdraw: "))
                            account.withdraw(amount)
                        except ValueError:
                            print(" Please enter a valid number.")

                    elif choice == "3":
                        account.check_balance()

                    elif choice == "4":
                        print(" Logging out...")
                        break

                    elif choice== "5":
                        print(" Exiting system. Goodbye! ")
                        sys.exit()  # Exit program immediately

                    else:
                        print(" Invalid option. Try again.")

        elif choice == "3":
            print(" Exiting system. Goodbye! ")
            sys.exit()  

        else:
            print(" Invalid choice. Please select 1, 2, or 3.")

main()