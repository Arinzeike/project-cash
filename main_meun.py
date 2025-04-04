
import csv
import os
import random
import getpass
from creater import create_user
from sign_in import sign_in
def main_menu():
    while True:
        print("===================================")
        print("   Welcome to Our Banking System   ")
        print("===================================")
        print("Please follow the instructions.")
        print("\n1. Create an Account")
        print("2. Sign In")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            create_user()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            print("Have a blessed day.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def validate_user(account_number, pin):
    if not os.path.isfile('account_users.csv'):
        print("No accounts found. Please create an account first.")
        return False

    with open('account_users.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Account Number'] == account_number and row['PIN'] == pin:
                return True
    return False

def generate_account_number():
    return random.randint(1000000000, 9999999999)

def save_user_info(full_name, pin, account_number):
    file_exists = os.path.isfile('account_users.csv')
    
    with open('account_users.csv', 'a', newline='') as csvfile:
        fieldnames = ['Full Name', 'PIN', 'Account Number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({'Full Name': full_name, 'PIN': pin, 'Account Number': account_number})

def generate_account_file(full_name, pin, account_number):
    filename = f"Account_{full_name}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("🎉 Account Successfully Created!\n")
        file.write("===============================\n")
        file.write(f"Full Name     : {full_name}\n")
        file.write(f"Account Number: {account_number}\n")
        file.write(f"PIN           : {pin}\n")
        file.write("===============================\n")
        file.write("📌 Please keep this file safe.\n")

if __name__ == "__main__":
    main_menu()
