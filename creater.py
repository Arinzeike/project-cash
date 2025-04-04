import csv
import os
import random
import getpass
from sign_in import sign_in

def create_user():
    while True:
        first_name = input("Enter your first name: ").strip()
        if not first_name:
            print("First name cannot be empty. Please try again.")
        elif not first_name.isalpha():
            print("First name must contain only letters. Please try again.")
        else:
            break

    while True:
        last_name = input("Enter your last name: ").strip()
        if not last_name:
            print("Last name cannot be empty. Please try again.")
        elif not last_name.isalpha():
            print("Last name must contain only letters. Please try again.")
        else:
            break

    full_name = first_name + " " + last_name

    # Create and validate a 4-digit pin
    while True:
        pin = getpass.getpass("Create a 4-digit pin: ")
        if pin.isdigit() and len(pin) == 4:
            break
        else:
            print("Pin must be a 4-digit number. Please try again.")

    account_number = str(generate_account_number())
    initial_balance = 0.0

    save_user_info(full_name, pin, account_number, initial_balance)
    generate_account_file(full_name, pin, account_number, initial_balance)

    print(f"\n🎉 Account created successfully! WITH RINZEY'S BANK 🎉")
    print(f"\n📄 Account details saved as 'Account_{full_name}.txt'")
    print(f"\n🔏 KINDLY KEEP IT SAFE 🔏")

    # Ask the user to sign in after creating an account
    print("\n🔐 Now, let's sign you into your new account!")

    sign_in()

def generate_account_number():
    return random.randint(1000000000, 9999999999)

def save_user_info(full_name, pin, account_number, balance):
    file_exists = os.path.isfile('me_info.csv')
    
    with open('me_info.csv', 'a', newline='') as csvfile:
        fieldnames = ['Full Name', 'PIN', 'Account Number', 'Balance']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'Full Name': full_name,
            'PIN': pin,
            'Account Number': account_number,
            'Balance': balance
        })

def generate_account_file(full_name, pin, account_number, balance):
    filename = f"Account_{full_name}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("🎉 Account Successfully Created!\n")
        file.write("===============================\n")
        file.write(f"Full Name     : {full_name}\n")
        file.write(f"Account Number: {account_number}\n")
        file.write(f"PIN           : {pin}\n")
        file.write(f"Balance       : ₦{balance:.2f}\n")
        file.write("===============================\n")
        file.write("📌 Please keep this file safe.\n")

if __name__ == "__main__":
    create_user()

