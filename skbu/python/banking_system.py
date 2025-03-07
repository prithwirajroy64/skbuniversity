





# import platform
# import subprocess
# import tkinter as tk
# from tkinter import messagebox
# Function to clear console
# def clear_console():
#     if platform.system() == "Windows":
#         os.system('cls')  # Windows

# # Function to show popup
# def show_popup(msg):
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window
#     messagebox.showinfo("Popup", msg)
#     root.destroy()

# Function to open terminal and run the current Python file
# def open_terminal():
#     # For Windows, ensure the script path is correctly quoted
#     if platform.system() == "Windows":
#         # No extra quotes around the path, just pass the correct path
#         subprocess.run(['start', 'cmd', '/K', 'python D:\\skbu\\python\\banking_system.py'], shell=True)

### Clear the console
# clear_console()

### Show the popup
# show_popup()

### Open terminal and run the script
import os
import sys
import time
import getpass
import random


class Banking_sys:
    bank_name = "Roy Finance Bank ltd."
    users_db = {}

    def __init__(self, name):
        self.name = name
        self.balance = 0
        
        
    def set_password(self):
        self.password = getpass.getpass(f"Set your password: ")

    def display_info(self):
        self.ac_number= random.randint(1000000000,9999999999)
        self.ifsc_number = random.randint(1000000,9999999)
        print(f"\nWelcome {self.name} to {self.bank_name}!".upper())
        print("---------------------------------------------")
        print(f"User Name: {self.name}")
        print(f"A/c Number: {self.ac_number}")
        print(f"IFSC Number: RFBL{self.ifsc_number}")
        print(f"Bank Name: {self.bank_name}\n\n")
        

    def add_cash(self, amount):
        self.balance += amount
        print("\n\nProccessing...")
        time.sleep(1)
        print(f"\nYou have successfully added ₹{amount}.0")
        time.sleep(3)
        os.system('cls')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("\n\nProccessing...")
            time.sleep(1)
            print(f"\nYou have successfully withdraw ₹{amount}.0")
        else:
            print("\nProccessing...")
            time.sleep(1)
            print("\nInsufficient balance!")
        time.sleep(3)
        os.system('cls')

    def check_balance(self):
        print("\n\nProccessing...")
        time.sleep(1)
        print(f"\nYour current balance is ₹{self.balance}.0")
        time.sleep(5)
        os.system('cls')

    @classmethod
    def create_account(cls):
        os.system('cls')
        print("Creating Account ------------------------------")
        name = input("\nEnter your name: ")
        if name in cls.users_db:
            print("Account already exists for this name. Please log in.")
            time.sleep(1)
            os.system('cls')
        else:
            new_user = Banking_sys(name)  # Create a new object for the user
            new_user.set_password()
            cls.users_db[name] = new_user  # Store the user object in the dictionary
            print(f"\nAccount creating.......")
            time.sleep(2)
            print(f"Account created successfully for {name}.")
            time.sleep(2)
            os.system('cls')

    @classmethod
    def login(cls):
        os.system('cls')
        print("Log in ------------------------------")
        name = input("\nEnter your name: ")
        if name in cls.users_db:
            password = input(f"Enter password: ")
            if password == cls.users_db[name].password:
                print("log in ........")
                time.sleep(2)
                print(f"\nLogged in successfully as {name}.\n")
                time.sleep(2)
                os.system('cls')
                user = cls.users_db[name]  # Retrieve the user object
                user.display_info()
                return user  # Return the user object for further operations
            else:
                print("Incorrect password. Please try again.")
                time.sleep(1)
                os.system('cls')
        else:
            print("Account does not exist. Please create an account first.")
            print("......")
            time.sleep(4)
            os.system('cls')
        
        return None

    @classmethod
    def perform_operations(cls):
        while True:
            # os.system('cls')
            action = input("\n--- Roy Finance Bank ltd.---\n1. Login\n2. Create an Account\n3. Exit\nEnter your choice: ")

            if action == '1':
                user = cls.login()
                if user:
                    while True:
                        print("--- Account Menu ---")
                        print("1. Deposit")
                        print("2. Withdraw")
                        print("3. Check Balance")
                        print("4. Log out")
                        option = input("Enter your choice: ")

                        if option == '1':
                            amount = int(input("Enter the amount to Deposit: "))
                            user.add_cash(amount)
                        elif option == '2':
                            amount = int(input("Enter the amount to Withdraw: "))
                            user.withdraw(amount)
                        elif option == '3':
                            user.check_balance()
                        elif option == '4':
                            os.system('cls')
                            print(f"Logging out {user.name}...\n")
                            time.sleep(1)
                            os.system('cls')
                            break
                        else:
                            print("Invalid choice! Please select a valid operation.")
                            time.sleep(1)
                            os.system('cls')
            elif action == '2':
                cls.create_account()
            elif action == '3':
                os.system('cls')
                print("BYE!")
                print("Closing the system......")
                time.sleep(1)
                os.system('cls')
                sys.exit()
            else:
                print("Invalid choice, please select 1 or 2.")
                time.sleep(1)
                os.system('cls')

Banking_sys.perform_operations()

