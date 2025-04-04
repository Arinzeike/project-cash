# import csv
# import os
# import getpass

# def sign_in():
#     attempts = 0

#     while attempts < 3:
#         account_number = input("Enter your Account number: ").strip()
#         pin = getpass.getpass("Enter your 4-digit pin: ").strip()

#         if not account_number.isdigit() or not pin.isdigit():
#             print("⚠️ Please enter valid numeric values.")
#             attempts += 1
#             continue

#         if validate_user(account_number, pin):
#             print("\n✅ Sign in successful! Welcome to your account.")
#             print("\nSelect an option:")
#             print("1. Check Balance")
#             print("2. Withdraw")
#             print("3. Pay Bills")
#             print("4. Deposit")
#             print("5. Exit")
#             return
#         else:
#             print("❌ Incorrect account number or PIN.")
#             attempts += 1

#     print("\n🚫 Maximum attempts reached. Access denied.")

# def validate_user(account_number, pin):
#     if not os.path.isfile('me_info.csv'):
#         print("⚠️ No accounts found. Please create an account first.")
#         return False

#     with open('me_info.csv', 'r', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Account Number'] == account_number and row['PIN'] == pin:
#                 return True
#     return False

# # 🔽 This runs the login function when the script is executed
# if __name__ == "__main__":
#     sign_in()


import csv
import os
import getpass

def sign_in():
    attempts = 0

    while attempts < 3:
        account_number = input("Enter your Account number: ").strip()
        pin = getpass.getpass("Enter your 4-digit pin: ").strip()

        if not account_number.isdigit() or not pin.isdigit():
            print("⚠️ Please enter valid numeric values.")
            attempts += 1
            continue

        user_name = validate_user(account_number, pin)
        if user_name:
            print(f"\n✅ Sign in successful!")
            print(f"\n {user_name}  Welcome to your account")
            print("\nSelect an option:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Pay Bills")
            print("4. Deposit")
            print("5. Exit")
            return
        else:
            print("❌ Incorrect account number or PIN.")
            attempts += 1

    print("\n🚫 Maximum attempts reached. Access denied.")

def validate_user(account_number, pin):
    if not os.path.isfile('me_info.csv'):
        print("⚠️ No accounts found. Please create an account first.")
        return False

    with open('me_info.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Account Number'] == account_number and row['PIN'] == pin:
                return row['Full Name']  # return user's name
    return False

# 🔽 This runs the login function when the script is executed
if __name__ == "__main__":
    sign_in()
