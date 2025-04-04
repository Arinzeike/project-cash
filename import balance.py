import balance
import bills
import deposit
import  withdrawal
import exit
import csv
def sign_in():
    count = 0

    def check_credentials(account_number, pin):
        with open('account_users.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if int(row['Account Number']) == account_number and int(row['PIN']) == pin:
                    return True
        return False

    while count < 3:
        try:
            account_number = int(input("Enter Account Number: "))
            pin = int(input("Enter Account PIN: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if check_credentials(account_number, pin):
            print("Welcome to your account!")
            print("1 for balance \n"
                  "2 for withdrawal \n"
                  "3 pay bills \n"
                  "4 deposit \n"
                  "5 exit")
#             # stage 2 menu
#     choice = int(input("choose option: "))
# # call balance function
#     if choice == 1:
#         balance.balance(initial_balance)
# # call withdrawal function
#     if choice == 2:
#         amount = int(input("enter amount: "))
#         if amount > initial_balance:
#             print("insufficient fund")
#         else:
#             initial_balance = withdrawal.withdraw(initial_balance,amount)
# # call deposit function
#     if choice == 4:
#         depo = int(input("enter deposit amount: "))
#         initial_balance = deposit.deposit(initial_balance,depo)
# # call bill function
#     if choice == 3:
#         bills.bills()
#         bill_option = int(input("enter option: "))
#         bill_amount = int(input("enter bill amount"))
#         if bill_amount > initial_balance:
#             print("insufficient funds")
#         else:

#             bills.calc_bill(initial_balance,bill_amount)

#     if choice >= 5 :
#         exit.exitapp()

        else:
            print("<<<<<Incorrect Details>>>>")
            count += 1

        if count == 3:
            print("Maximum attempts reached. Access denied.")
            break

if __name__ == "__main__":
    sign_in()
   
