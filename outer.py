# # # import balance
# # # import bills
# # # import deposit
# # # import  withdrawal
# # # import exit
# # # import csv
# # # init_balance= 0
# # # def sign_in():
# # #     count = 0

# # #     def check_credentials(account_number, pin):
# # #         with open('user_info.csv', newline='') as csvfile:
# # #             reader = csv.DictReader(csvfile)
# # #             for row in reader:
# # #                 if int(row['Account Number']) == account_number and int(row['PIN']) == pin:
# # #                     return True
# # #         return False

# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         if check_credentials(account_number, pin):
# # #             print("Welcome to your account!")
# # #             print("1 for balance \n"
# # #                   "2 for withdrawal \n"
# # #                   "3 pay bills \n"
# # #                   "4 deposit \n"
# # #                   "5 exit")
# # #             choice = int(input("choose option: "))
# # #             if choice == 1:
# # #                  balance.balance(init_balance)
# # #             # call withdrawal function
# # #             if choice == 2:
# # #                 amount = int(input("enter amount: "))
# # #                 if amount > init_balance:
# # #                     print("insufficient fund")
# # #                 else:
# # #                     init_balance = withdrawal.withdraw(init_balance,amount)
# # #             # call deposit function
# # #             if choice == 4:
# # #                 depo = int(input("enter deposit amount: "))
# # #                 init_balance = deposit.deposit(init_balance,depo)
# # #             # call bill function
# # #             if choice == 3:
# # #                 bills.bills()
# # #                 bill_option = int(input("enter option: "))
# # #                 bill_amount = int(input("enter bill amount"))
# # #                 if bill_amount > init_balance:
# # #                     print("insufficient funds")
# # #                 else:
# # #                     bills.calc_bill(init_balance,bill_amount)

# # #             if choice >= 5 :
# # #                 exit.exitapp()
# # #         #     break

# # #         # else:
# # #         #     print("<<<<<Incorrect Details>>>>")
# # #         #     count += 1

# # #         # if count == 3:
# # #         #     print("Maximum attempts reached. Access denied.")
# # #         #     break
# # # #         choice = int(input("choose option: "))
# # # #         if choice == 1:
# # # #             balance.balance(initial_balance)
# # # # # call withdrawal function
# # # #         if choice == 2:
# # # #              amount = int(input("enter amount: "))
# # # #             if amount > initial_balance:
# # # #                 print("insufficient fund")
# # # #             else:
# # # #                 initial_balance = withdrawal.withdraw(initial_balance,amount)
# # # # # call deposit function
# # # #         if choice == 4:
# # # #             depo = int(input("enter deposit amount: "))
# # # #             initial_balance = deposit.deposit(initial_balance,depo)
# # # # # call bill function
# # # #         if choice == 3:
# # # #             bills.bills()
# # # #             bill_option = int(input("enter option: "))
# # # #             bill_amount = int(input("enter bill amount"))
# # # #             if bill_amount > initial_balance:
# # # #                 print("insufficient funds")
# # # #         else:
# # # #             bills.calc_bill(initial_balance,bill_amount)

# # # #         if choice >= 5 :
# # # #             exit.exitapp()
# # # if __name__ == "__main__":
# # #     sign_in()
   

# # # import csv

# # # # Assuming the necessary modules are imported correctly
# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit

# # # init_balance = 0

# # # def sign_in():
# # #     count = 0

# # #     def check_credentials(account_number, pin):
# # #         with open('user_info.csv', newline='') as csvfile:
# # #             reader = csv.DictReader(csvfile)
# # #             for row in reader:
# # #                 if int(row['Account Number']) == account_number and int(row['PIN']) == pin:
# # #                     return True
# # #         return False

# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         if check_credentials(account_number, pin):
# # #             print("Welcome to your account!")
# # #             global init_balance  # Use the global variable for balance

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 5.")
# # #                     continue

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = int(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = int(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = int(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     break
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 5.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()
# # # import csv

# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:

# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = ['Account Number', 'PIN', 'Balance']
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         return True, float(user['Balance'])
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 5.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 5.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()

# # # import csv

# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = ['Account Number', 'PIN', 'Balance']
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         return True, float(user['Balance'])
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 5.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 5.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()
# # # E DEY WORK
# # # import csv

# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         return True, float(user['Balance'])
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 5.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 5.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()


# # # import csv

# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit
# # # import transfer
# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         try:
# # #             balance = float(user['Balance'])
# # #         except (ValueError, TypeError):
# # #             balance = 0.0
# # #         return True, balance
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit"
# # #                       "6 to transfer \n")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 5.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 6:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = transfer.transfer(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                     except ValueError as e:
# # #                         print(e)
# # #                         continue
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 5.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()


# # # import csv

# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit
# # # import transfer

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         try:
# # #             balance = float(user['Balance'])
# # #         except (ValueError, TypeError):
# # #             balance = 0.0
# # #         return True, balance
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit \n"
# # #                       "6 to transfer \n")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 6.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 elif choice == 6:
# # #                     try:
# # #                         receiver_account = int(input("Enter receiver's account number: "))
# # #                         amount = float(input("Enter amount to transfer: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, get_user_data)
# # #                             print(f"Transfer successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                     except ValueError as e:
# # #                         print(e)
# # #                         continue
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 6.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()


# # # import csv
# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit
# # # import transfer

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         try:
# # #             balance = float(user['Balance'])
# # #         except (ValueError, TypeError):
# # #             balance = 0.0
# # #         return True, balance
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit \n"
# # #                       "6 to transfer \n")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 6.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 elif choice == 6:
# # #                     try:
# # #                         receiver_account = int(input("Enter receiver's account number: "))
# # #                         amount = float(input("Enter amount to transfer: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data)
# # #                             print(f"Transfer successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                     except ValueError as e:
# # #                         print(e)
# # #                         continue
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 6.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()
# # # import csv
# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit
# # # import transfer

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         try:
# # #             balance = float(user['Balance'])
# # #         except (ValueError, TypeError):
# # #             balance = 0.0
# # #         return True, balance
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit \n"
# # #                       "6 to transfer \n")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 6.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 elif choice == 6:
# # #                     try:
# # #                         receiver_account = int(input("Enter receiver's account number: "))
# # #                         amount = float(input("Enter amount to transfer: "))
# # #                         sender_user, _ = get_user_data(account_number)  # Fetch sender's user data
# # #                         if not sender_user:
# # #                             raise ValueError("Sender account not found.")  # Raise error if sender's account is not found

# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance, _ = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data)
# # #                             print(f"Transfer successful. New balance: {init_balance}")
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError as ve:
# # #                         if 'receiver_account' in str(ve):
# # #                             print("Invalid input for receiver's account number. Please enter a valid numeric value.")
# # #                         elif 'amount' in str(ve):
# # #                             print("Invalid input for transfer amount. Please enter a valid numeric value.")
# # #                         else:
# # #                             print(ve)  # Print any other ValueError
# # #                     except Exception as e:
# # #                         print("An unexpected error occurred:", e)
# # #                         continue
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 6.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()
# # # import csv
# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit
# # # import transfer

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         try:
# # #             balance = float(user['Balance'])
# # #         except (ValueError, TypeError):
# # #             balance = 0.0
# # #         return True, balance
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit \n"
# # #                       "6 to transfer \n")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 6.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 elif choice == 6:
# # #                     try:
# # #                         sender_account = int(input("Enter your account number: "))
# # #                         receiver_account = int(input("Enter receiver's account number: "))
# # #                         amount = float(input("Enter amount to transfer: "))
                        
# # #                         sender_user, _ = get_user_data(sender_account)  # Fetch sender's user data
# # #                         if not sender_user:
# # #                             raise ValueError("Sender account not found.")  # Raise error if sender's account is not found
                        
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, sender_account, receiver_account, update_user_data, get_user_data)
# # #                             print(f"Transfer successful. Your balance: {new_sender_balance}")
# # #                             update_user_data(sender_account, new_sender_balance, users)
# # #                             update_user_data(receiver_account, new_receiver_balance, users)
# # #                     except ValueError as ve:
# # #                         if 'receiver_account' in str(ve):
# # #                             print("Invalid input for receiver's account number. Please enter a valid numeric value.")
# # #                         elif 'amount' in str(ve):
# # #                             print("Invalid input for transfer amount. Please enter a valid numeric value.")
# # #                         else:
# # #                             print(ve)  # Print any other ValueError
# # #                     except Exception as e:
# # #                         print("An unexpected error occurred:", e)
# # #                         continue
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 6.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()



# # # import csv
# # # import balance
# # # import bills
# # # import deposit
# # # import withdrawal
# # # import exit
# # # import transfer
# # # import account_statement

# # # def get_user_data(account_number):
# # #     with open('me_info.csv', newline='') as csvfile:
# # #         reader = csv.DictReader(csvfile)
# # #         users = [row for row in reader]
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             return user, users
# # #     return None, users

# # # def update_user_data(account_number, new_balance, users):
# # #     for user in users:
# # #         if int(user['Account Number']) == account_number:
# # #             user['Balance'] = str(new_balance)
# # #             break
# # #     with open('me_info.csv', 'w', newline='') as csvfile:
# # #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# # #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# # #         writer.writeheader()
# # #         writer.writerows(users)

# # # def check_credentials(account_number, pin):
# # #     user, _ = get_user_data(account_number)
# # #     if user and int(user['PIN']) == pin:
# # #         try:
# # #             balance = float(user['Balance'])
# # #         except (ValueError, TypeError):
# # #             balance = 0.0
# # #         return True, balance
# # #     return False, 0.0

# # # def sign_in():
# # #     count = 0
# # #     while count < 3:
# # #         try:
# # #             account_number = int(input("Enter Account Number: "))
# # #             pin = int(input("Enter Account PIN: "))
# # #         except ValueError:
# # #             print("Invalid input. Please enter numeric values.")
# # #             continue

# # #         authenticated, init_balance = check_credentials(account_number, pin)
# # #         if authenticated:
# # #             print("Welcome to your account!")

# # #             while True:
# # #                 print("1 for balance \n"
# # #                       "2 for withdrawal \n"
# # #                       "3 to pay bills \n"
# # #                       "4 to deposit \n"
# # #                       "5 to exit \n"
# # #                       "6 to transfer \n")
# # #                 try:
# # #                     choice = int(input("Choose an option: "))
# # #                 except ValueError:
# # #                     print("Invalid input. Please enter a number between 1 and 6.")
# # #                     continue

# # #                 user, users = get_user_data(account_number)

# # #                 if choice == 1:
# # #                     balance.balance(init_balance)
# # #                 elif choice == 2:
# # #                     try:
# # #                         amount = float(input("Enter amount: "))
# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = withdrawal.withdraw(init_balance, amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 3:
# # #                     bills.bills()
# # #                     try:
# # #                         bill_option = int(input("Enter bill option: "))
# # #                         bill_amount = float(input("Enter bill amount: "))
# # #                         if bill_amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# # #                             update_user_data(account_number, init_balance, users)
# # #                     except ValueError:
# # #                         print("Invalid input. Please enter numeric values.")
# # #                 elif choice == 4:
# # #                     try:
# # #                         depo = float(input("Enter deposit amount: "))
# # #                         init_balance = deposit.deposit(init_balance, depo)
# # #                         update_user_data(account_number, init_balance, users)
# # #                         print(f"Deposit successful. New balance: {init_balance}")
# # #                     except ValueError:
# # #                         print("Invalid amount. Please enter a numeric value.")
# # #                 elif choice == 5:
# # #                     exit.exitapp()
# # #                     update_user_data(account_number, init_balance, users)
# # #                     break
# # #                 elif choice == 6:
# # #                     try:
# # #                         receiver_account = int(input("Enter receiver's account number: "))
# # #                         amount = float(input("Enter amount to transfer: "))

# # #                         if amount > init_balance:
# # #                             print("Insufficient funds.")
# # #                         else:
# # #                             new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
# # #                             print(f"Transfer successful. Your Balance: {new_sender_balance}")
# # #                             init_balance = new_sender_balance  # Update the current session balance
# # #                             update_user_data(account_number, new_sender_balance, users)
# # #                             # Update receiver user data separately to ensure consistency
# # #                             receiver_user, receiver_users = get_user_data(receiver_account)
# # #                             update_user_data(receiver_account, new_receiver_balance, receiver_users)
# # #                     except ValueError as ve:
# # #                         if 'receiver_account' in str(ve):
# # #                             print("Invalid input for receiver's account number. Please enter a valid numeric value.")
# # #                         elif 'amount' in str(ve):
# # #                             print("Invalid input for transfer amount. Please enter a valid numeric value.")
# # #                         else:
# # #                             print(ve)  # Print any other ValueError
# # #                     except Exception as e:
# # #                         print("An unexpected error occurred:", e)
# # #                         continue
# # #                 else:
# # #                     print("Invalid choice. Please enter a number between 1 and 6.")
# # #         else:
# # #             print("<<<<<Incorrect Details>>>>")
# # #             count += 1

# # #         if count == 3:
# # #             print("Maximum attempts reached. Access denied.")
# # #             break

# # # if __name__ == "__main__":
# # #     sign_in()


# # import csv
# # import time
# # import balance
# # import bills
# # import deposit
# # import withdrawal
# # import exit
# # import transfer
# # import os
# # from account_statement import account_statement


# # def get_user_data(account_number):
# #     with open('me_info.csv', newline='') as csvfile:
# #         reader = csv.DictReader(csvfile)
# #         users = [row for row in reader]
# #     for user in users:
# #         if int(user['Account Number']) == account_number:
# #             return user, users
# #     return None, users

# # def update_user_data(account_number, new_balance, users):
# #     for user in users:
# #         if int(user['Account Number']) == account_number:
# #             user['Balance'] = str(new_balance)
# #             break
# #     with open('me_info.csv', 'w', newline='') as csvfile:
# #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #         writer.writeheader()
# #         writer.writerows(users)

# # def log_activity(account_number, activity):
# #     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
# #     with open('activity_log.csv', 'a', newline='') as logfile:
# #         fieldnames = ['Timestamp', 'Account Number', 'Activity']
# #         writer = csv.DictWriter(logfile, fieldnames=fieldnames)
# #         writer.writerow({'Timestamp': timestamp, 'Account Number': account_number, 'Activity': activity})

# # def check_credentials(account_number, pin):
# #     user, _ = get_user_data(account_number)
# #     if user and int(user['PIN']) == pin:
# #         try:
# #             balance = float(user['Balance'])
# #         except (ValueError, TypeError):
# #             balance = 0.0
# #         return True, balance
# #     return False, 0.0

# # # def account_statement(account_number):
# # #     activities = []
# # #     try:
# # #         with open('activity_log.csv', newline='') as logfile:
# # #             reader = csv.DictReader(logfile)
# # #             for row in reader:
# # #                 if int(row['Account Number']) == account_number:
# # #                     activities.append((row['Timestamp'], row['Activity']))
# # #     except FileNotFoundError:
# # #         print("Activity log file not found.")
# # #         return
    
# # #     if activities:
# # #         print(f"Account Statement for Account Number: {account_number}")
# # #         print("--------------------------------------------------")
# # #         for timestamp, activity in activities:
# # #             print(f"{timestamp}: {activity}")
# # #     else:
# # #         print("No activities found for this account.")

# # def sign_in():
# #     count = 0
# #     while count < 3:
# #         try:
# #             account_number = int(input("Enter Account Number: "))
# #             pin = int(input("Enter Account PIN: "))
# #         except ValueError:
# #             print("Invalid input. Please enter numeric values.")
# #             continue

# #         authenticated, init_balance = check_credentials(account_number, pin)
# #         if authenticated:
# #             print("Welcome to your account!")

# #             log_activity(account_number, 'Sign in')

# #             while True:
# #                 print("1 for balance \n"
# #                       "2 for withdrawal \n"
# #                       "3 to pay bills \n"
# #                       "4 to deposit \n"
# #                       "5 to exit \n"
# #                       "6 to transfer \n"
# #                       "7 for account statement \n")
# #                 try:
# #                     choice = int(input("Choose an option: "))
# #                 except ValueError:
# #                     print("Invalid input. Please enter a number between 1 and 7.")
# #                     continue

# #                 user, users = get_user_data(account_number)

# #                 if choice == 1:
# #                     balance.balance(init_balance)
# #                     log_activity(account_number, 'Check balance')
# #                 elif choice == 2:
# #                     try:
# #                         amount = float(input("Enter amount: "))
# #                         if amount > init_balance:
# #                             print("Insufficient funds.")
# #                         else:
# #                             init_balance = withdrawal.withdraw(init_balance, amount)
# #                             update_user_data(account_number, init_balance, users)
# #                             log_activity(account_number, f'Withdrawal of {amount}')
# #                     except ValueError:
# #                         print("Invalid amount. Please enter a numeric value.")
# #                 elif choice == 3:
# #                     bills.bills()
# #                     try:
# #                         bill_option = int(input("Enter bill option: "))
# #                         bill_amount = float(input("Enter bill amount: "))
# #                         if bill_amount > init_balance:
# #                             print("Insufficient funds.")
# #                         else:
# #                             init_balance = bills.calc_bill(init_balance, bill_amount)
# #                             update_user_data(account_number, init_balance, users)
# #                             log_activity(account_number, f'Payment of bill: {bill_amount}')
# #                     except ValueError:
# #                         print("Invalid input. Please enter numeric values.")
# #                 elif choice == 4:
# #                     try:
# #                         depo = float(input("Enter deposit amount: "))
# #                         init_balance = deposit.deposit(init_balance, depo)
# #                         update_user_data(account_number, init_balance, users)
# #                         print(f"Deposit successful. New balance: {init_balance}")
# #                         log_activity(account_number, f'Deposit of {depo}')
# #                     except ValueError:
# #                         print("Invalid amount. Please enter a numeric value.")
# #                 elif choice == 5:
# #                     exit.exitapp()
# #                     update_user_data(account_number, init_balance, users)
# #                     log_activity(account_number, 'Exit')
# #                     break
# #                 elif choice == 6:
# #                     try:
# #                         receiver_account = int(input("Enter receiver's account number: "))
# #                         amount = float(input("Enter amount to transfer: "))

# #                         if amount > init_balance:
# #                             print("Insufficient funds.")
# #                         else:
# #                             new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
# #                             print(f"Transfer successful. New sender balance: {new_sender_balance}, New receiver balance: {new_receiver_balance}")
# #                             init_balance = new_sender_balance  # Update the current session balance
# #                             update_user_data(account_number, new_sender_balance, users)
# #                             # Update receiver user data separately to ensure consistency
# #                             receiver_user, receiver_users = get_user_data(receiver_account)
# #                             update_user_data(receiver_account, new_receiver_balance, receiver_users)
# #                             log_activity(account_number, f'Transfer of {amount} to {receiver_account}')
# #                     except ValueError as ve:
# #                         if 'receiver_account' in str(ve):
# #                             print("Invalid input for receiver's account number. Please enter a valid numeric value.")
# #                         elif 'amount' in str(ve):
# #                             print("Invalid input for transfer amount. Please enter a valid numeric value.")
# #                         else:
# #                             print(ve)  # Print any other ValueError
# #                     except Exception as e:
# #                         print("An unexpected error occurred:", e)
# #                         continue
# #                 elif choice == 7:
# #                     account_statement(account_number)
                    
# #                 else:
# #                     print("Invalid choice. Please enter a number between 1 and 7.")
# #         else:
# #             print("<<<<<Incorrect Details>>>>")
# #             count += 1

# #         if count == 3:
# #             print("Maximum attempts reached. Access denied.")
# #             break

# # if __name__ == "__main__":
# #     # Check if activity log file exists, create it if not
# #     if not os.path.isfile('activity_log.csv'):
# #         with open('activity_log.csv', 'w', newline='') as logfile:
# #             fieldnames = ['Timestamp', 'Account Number', 'Activity']
# #             writer = csv.DictWriter(logfile, fieldnames=fieldnames)
# #             writer.writeheader()

# #     sign_in()

# # import csv
# # import time
# # import balance
# # import bills
# # import deposit
# # import withdrawal
# # import exit
# # import transfer
# # import os
# # from account_statement import account_statement

# # def get_user_data(account_number):
# #     with open('me_info.csv', newline='') as csvfile:
# #         reader = csv.DictReader(csvfile)
# #         users = [row for row in reader]
# #     for user in users:
# #         if int(user['Account Number']) == account_number:
# #             return user, users
# #     return None, users

# # def update_user_data(account_number, new_balance, users):
# #     for user in users:
# #         if int(user['Account Number']) == account_number:
# #             user['Balance'] = str(new_balance)
# #             break
# #     with open('me_info.csv', 'w', newline='') as csvfile:
# #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #         writer.writeheader()
# #         writer.writerows(users)

# # def log_activity(account_number, activity):
# #     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
# #     with open('activity_log.csv', 'a', newline='') as logfile:
# #         fieldnames = ['Timestamp', 'Account Number', 'Activity']
# #         writer = csv.DictWriter(logfile, fieldnames=fieldnames)
# #         writer.writerow({'Timestamp': timestamp, 'Account Number': account_number, 'Activity': activity})

# # def check_credentials(account_number, pin):
# #     user, _ = get_user_data(account_number)
# #     if user and int(user['PIN']) == pin:
# #         try:
# #             balance = float(user['Balance'])
# #         except (ValueError, TypeError):
# #             balance = 0.0
# #         return True, balance
# #     return False, 0.0

# # def main_menu(init_balance, account_number, users):
# #     while True:
# #         print("1 for balance \n"
# #               "2 for withdrawal \n"
# #               "3 to pay bills \n"
# #               "4 to deposit \n"
# #               "5 to exit \n"
# #               "6 to transfer \n"
# #               "7 for account statement \n")
# #         try:
# #             choice = int(input("Choose an option: "))
# #         except ValueError:
# #             print("Invalid input. Please enter a number between 1 and 7.")
# #             continue

# #         if choice == 1:
# #             balance.balance(init_balance)
# #             log_activity(account_number, 'Check balance')
# #         elif choice == 2:
# #             try:
# #                 amount = float(input("Enter amount: "))
# #                 if amount > init_balance:
# #                     print("Insufficient funds.")
# #                 else:
# #                     init_balance = withdrawal.withdraw(init_balance, amount)
# #                     update_user_data(account_number, init_balance, users)
# #                     log_activity(account_number, f'Withdrawal of {amount}')
# #             except ValueError:
# #                 print("Invalid amount. Please enter a numeric value.")
# #         elif choice == 3:
# #             bills.bills()
# #             try:
# #                 bill_option = int(input("Enter bill option: "))
# #                 bill_amount = float(input("Enter bill amount: "))
# #                 if bill_amount > init_balance:
# #                     print("Insufficient funds.")
# #                 else:
# #                     init_balance = bills.calc_bill(init_balance, bill_amount)
# #                     update_user_data(account_number, init_balance, users)
# #                     log_activity(account_number, f'Payment of bill: {bill_amount}')
# #             except ValueError:
# #                 print("Invalid input. Please enter numeric values.")
# #         elif choice == 4:
# #             try:
# #                 depo = float(input("Enter deposit amount: "))
# #                 init_balance = deposit.deposit(init_balance, depo)
# #                 update_user_data(account_number, init_balance, users)
# #                 print(f"Deposit successful. New balance: {init_balance}")
# #                 log_activity(account_number, f'Deposit of {depo}')
# #             except ValueError:
# #                 print("Invalid amount. Please enter a numeric value.")
# #         elif choice == 5:
# #             exit.exitapp()
# #             update_user_data(account_number, init_balance, users)
# #             log_activity(account_number, 'Exit')
# #             print("Thanks for your patronage!")
# #             break
# #         elif choice == 6:
# #             try:
# #                 receiver_account = int(input("Enter receiver's account number: "))
# #                 amount = float(input("Enter amount to transfer: "))

# #                 if amount > init_balance:
# #                     print("Insufficient funds.")
# #                 else:
# #                     new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
# #                     print(f"Transfer successful. New sender balance: {new_sender_balance}, New receiver balance: {new_receiver_balance}")
# #                     init_balance = new_sender_balance  # Update the current session balance
# #                     update_user_data(account_number, new_sender_balance, users)
# #                     # Update receiver user data separately to ensure consistency
# #                     receiver_user, receiver_users = get_user_data(receiver_account)
# #                     update_user_data(receiver_account, new_receiver_balance, receiver_users)
# #                     log_activity(account_number, f'Transfer of {amount} to {receiver_account}')
# #             except ValueError as ve:
# #                 if 'receiver_account' in str(ve):
# #                     print("Invalid input for receiver's account number. Please enter a valid numeric value.")
# #                 elif 'amount' in str(ve):
# #                     print("Invalid input for transfer amount. Please enter a valid numeric value.")
# #                 else:
# #                     print(ve)  # Print any other ValueError
# #             except Exception as e:
# #                 print("An unexpected error occurred:", e)
# #                 continue
# #         elif choice == 7:
# #             account_statement(account_number)
# #         else:
# #             print("Invalid choice. Please enter a number between 1 and 7.")

# #         another_option = input("Do you want to perform another operation? (y/n): ").strip().lower()
# #         if another_option not in ('y', 'yes'):
# #             print("Thanks for your patronage!")
# #             break

# # def sign_in():
# #     count = 0
# #     while count < 3:
# #         try:
# #             account_number = int(input("Enter Account Number: "))
# #             pin = int(input("Enter Account PIN: "))
# #         except ValueError:
# #             print("Invalid input. Please enter numeric values.")
# #             continue

# #         authenticated, init_balance = check_credentials(account_number, pin)
# #         if authenticated:
# #             print("Welcome to your account!")

# #             log_activity(account_number, 'Sign in')

# #             user, users = get_user_data(account_number)
# #             main_menu(init_balance, account_number, users)
# #             break
# #         else:
# #             print("<<<<<Incorrect Details>>>>")
# #             count += 1

# #         if count == 3:
# #             print("Maximum attempts reached. Access denied.")
# #             break

# # if __name__ == "__main__":
# #     # Check if activity log file exists, create it if not
# #     if not os.path.isfile('activity_log.csv'):
# #         with open('activity_log.csv', 'w', newline='') as logfile:
# #             fieldnames = ['Timestamp', 'Account Number', 'Activity']
# #             writer = csv.DictWriter(logfile, fieldnames=fieldnames)
# #             writer.writeheader()

# #     sign_in()



# # import csv
# # import time
# # import balance
# # import bills
# # import deposit
# # import withdrawal
# # import exit
# # import transfer
# # import os
# # from account_statement import account_statement

# # def get_user_data(account_number):
# #     with open('me_info.csv', newline='') as csvfile:
# #         reader = csv.DictReader(csvfile)
# #         users = [row for row in reader]
# #     for user in users:
# #         if int(user['Account Number']) == account_number:
# #             return user, users
# #     return None, users

# # def update_user_data(account_number, new_balance, users):
# #     for user in users:
# #         if int(user['Account Number']) == account_number:
# #             user['Balance'] = str(new_balance)
# #             break
# #     with open('me_info.csv', 'w', newline='') as csvfile:
# #         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
# #         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
# #         writer.writeheader()
# #         writer.writerows(users)

# # def log_activity(account_number, activity):
# #     timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
# #     with open('activity_log.csv', 'a', newline='') as logfile:
# #         fieldnames = ['Timestamp', 'Account Number', 'Activity']
# #         writer = csv.DictWriter(logfile, fieldnames=fieldnames)
# #         writer.writerow({'Timestamp': timestamp, 'Account Number': account_number, 'Activity': activity})

# # def check_credentials(account_number, pin):
# #     user, _ = get_user_data(account_number)
# #     if user and int(user['PIN']) == pin:
# #         try:
# #             balance = float(user['Balance'])
# #         except (ValueError, TypeError):
# #             balance = 0.0
# #         return True, balance
# #     return False, 0.0

# # def main_menu(init_balance, account_number, users):
# #     while True:
# #         print("1 for balance \n"
# #               "2 for withdrawal \n"
# #               "3 to pay bills \n"
# #               "4 to deposit \n"
# #               "5 to exit \n"
# #               "6 to transfer \n"
# #               "7 for account statement \n")
# #         try:
# #             choice = int(input("Choose an option: "))
# #         except ValueError:
# #             print("Invalid input. Please enter a number between 1 and 7.")
# #             continue

# #         if choice == 1:
# #             balance.balance(init_balance)
# #             log_activity(account_number, 'Check balance')
# #         elif choice == 2:
# #             try:
# #                 amount = float(input("Enter amount: "))
# #                 if amount > init_balance:
# #                     print("Insufficient funds.")
# #                 else:
# #                     init_balance = withdrawal.withdraw(init_balance, amount)
# #                     update_user_data(account_number, init_balance, users)
# #                     log_activity(account_number, f'Withdrawal of {amount}')
# #             except ValueError:
# #                 print("Invalid amount. Please enter a numeric value.")
# #         elif choice == 3:
# #             bills.bills()
# #             try:
# #                 bill_option = int(input("Enter bill option: "))
# #                 bill_amount = float(input("Enter bill amount: "))
# #                 if bill_amount > init_balance:
# #                     print("Insufficient funds.")
# #                 else:
# #                     init_balance = bills.calc_bill(init_balance, bill_amount)
# #                     update_user_data(account_number, init_balance, users)
# #                     log_activity(account_number, f'Payment of bill: {bill_amount}')
# #             except ValueError:
# #                 print("Invalid input. Please enter numeric values.")
# #         elif choice == 4:
# #             try:
# #                 depo = float(input("Enter deposit amount: "))
# #                 init_balance = deposit.deposit(init_balance, depo)
# #                 update_user_data(account_number, init_balance, users)
# #                 print(f"Deposit successful. New balance: {init_balance}")
# #                 log_activity(account_number, f'Deposit of {depo}')
# #             except ValueError:
# #                 print("Invalid amount. Please enter a numeric value.")
# #         elif choice == 5:
# #             exit.exitapp()
# #             update_user_data(account_number, init_balance, users)
# #             log_activity(account_number, 'Exit')
# #             print("Thanks for your patronage!")
# #             ask_to_print_statement(account_number)
# #             break
# #         elif choice == 6:
# #             try:
# #                 receiver_account = int(input("Enter receiver's account number: "))
# #                 amount = float(input("Enter amount to transfer: "))

# #                 if amount > init_balance:
# #                     print("Insufficient funds.")
# #                 else:
# #                     new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
# #                     print(f"Transfer successful. New sender balance: {new_sender_balance}, New receiver balance: {new_receiver_balance}")
# #                     init_balance = new_sender_balance  # Update the current session balance
# #                     update_user_data(account_number, new_sender_balance, users)
# #                     # Update receiver user data separately to ensure consistency
# #                     receiver_user, receiver_users = get_user_data(receiver_account)
# #                     update_user_data(receiver_account, new_receiver_balance, receiver_users)
# #                     log_activity(account_number, f'Transfer of {amount} to {receiver_account}')
# #             except ValueError as ve:
# #                 if 'receiver_account' in str(ve):
# #                     print("Invalid input for receiver's account number. Please enter a valid numeric value.")
# #                 elif 'amount' in str(ve):
# #                     print("Invalid input for transfer amount. Please enter a valid numeric value.")
# #                 else:
# #                     print(ve)  # Print any other ValueError
# #             except Exception as e:
# #                 print("An unexpected error occurred:", e)
# #                 continue
# #         elif choice == 7:
# #             account_statement(account_number)
# #         else:
# #             print("Invalid choice. Please enter a number between 1 and 7.")

# #         another_option = input("Do you want to perform another operation? (y/n): ").strip().lower()
# #         if another_option not in ('y', 'yes'):
# #             print("Thanks for your patronage!")
# #             ask_to_print_statement(account_number)
# #             break

# # def ask_to_print_statement(account_number):
# #     print_statement = input("Do you want to print your account statement? (y/n): ").strip().lower()
# #     if print_statement in ('y', 'yes'):
# #         account_statement(account_number)

# # def sign_in():
# #     count = 0
# #     while count < 3:
# #         try:
# #             account_number = int(input("Enter Account Number: "))
# #             pin = int(input("Enter Account PIN: "))
# #         except ValueError:
# #             print("Invalid input. Please enter numeric values.")
# #             continue

# #         authenticated, init_balance = check_credentials(account_number, pin)
# #         if authenticated:
# #             print("Welcome to your account!")

# #             log_activity(account_number, 'Sign in')

# #             user, users = get_user_data(account_number)
# #             main_menu(init_balance, account_number, users)
# #             break
# #         else:
# #             print("<<<<<Incorrect Details>>>>")
# #             count += 1

# #         if count == 3:
# #             print("Maximum attempts reached. Access denied.")
# #             break

# # if __name__ == "__main__":
# #     # Check if activity log file exists, create it if not
# #     if not os.path.isfile('activity_log.csv'):
# #         with open('activity_log.csv', 'w', newline='') as logfile:
# #             fieldnames = ['Timestamp', 'Account Number', 'Activity']
# #             writer = csv.DictWriter(logfile, fieldnames=fieldnames)
# #             writer.writeheader()

# #     sign_in()



# import csv
# import time
# import balance
# import bills
# import deposit
# import withdrawal
# import exit
# import transfer
# import os
# # from account_statement import account_statement, generate_pdf, log_activity

# def get_user_data(account_number):
#     with open('account_users.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         users = [row for row in reader]
#     for user in users:
#         if int(user['Account Number']) == account_number:
#             return user, users
#     return None, users

# def update_user_data(account_number, new_balance, users):
#     for user in users:
#         if int(user['Account Number']) == account_number:
#             user['Balance'] = str(new_balance)
#             break
#     with open('account_users.csv', 'w', newline='') as csvfile:
#         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(users)

# def check_credentials(account_number, pin):
#     user, _ = get_user_data(account_number)
#     if user and int(user['PIN']) == pin:
#         try:
#             balance = float(user['Balance'])
#         except (ValueError, TypeError):
#             balance = 0.0
#         return True, balance
#     return False, 0.0

# def main_menu(init_balance, account_number, users):
#     while True:
#         print("1 for balance \n"
#               "2 for withdrawal \n"
#               "3 to pay bills \n"
#               "4 to deposit \n"
#               "5 to exit \n"
#               "6 to transfer \n"
#               "7 for account statement \n")
#         try:
#             choice = int(input("Choose an option: "))
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 7.")
#             continue

#         if choice == 1:
#             balance.balance(init_balance)
#             log_activity(account_number, 'Check balance')
#         elif choice == 2:
#             try:
#                 amount = float(input("Enter amount: "))
#                 if amount > init_balance:
#                     print("Insufficient funds.")
#                 else:
#                     init_balance = withdrawal.withdraw(init_balance, amount)
#                     update_user_data(account_number, init_balance, users)
#                     log_activity(account_number, f'Withdrawal of {amount}')
#             except ValueError:
#                 print("Invalid amount. Please enter a numeric value.")
#         elif choice == 3:
#             bills.bills()
#             try:
#                 bill_option = int(input("Enter bill option: "))
#                 bill_amount = float(input("Enter bill amount: "))
#                 if bill_amount > init_balance:
#                     print("Insufficient funds.")
#                 else:
#                     init_balance = bills.calc_bill(init_balance, bill_amount)
#                     update_user_data(account_number, init_balance, users)
#                     log_activity(account_number, f'Payment of bill: {bill_amount}')
#             except ValueError:
#                 print("Invalid input. Please enter numeric values.")
#         elif choice == 4:
#             try:
#                 depo = float(input("Enter deposit amount: "))
#                 init_balance = deposit.deposit(init_balance, depo)
#                 update_user_data(account_number, init_balance, users)
#                 print(f"Deposit successful. New balance: {init_balance}")
#                 log_activity(account_number, f'Deposit of {depo}')
#             except ValueError:
#                 print("Invalid amount. Please enter a numeric value.")
#         elif choice == 5:
#             update_user_data(account_number, init_balance, users)
#             log_activity(account_number, 'Exit')
#             print("Thanks for your patronage!")
#             ask_to_print_statement(account_number)
#             break
#         elif choice == 6:
#             try:
#                 receiver_account = int(input("Enter receiver's account number: "))
#                 amount = float(input("Enter amount to transfer: "))

#                 if amount > init_balance:
#                     print("Insufficient funds.")
#                 else:
#                     new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
#                     print(f"Transfer successful. New sender balance: {new_sender_balance}, New receiver balance: {new_receiver_balance}")
#                     init_balance = new_sender_balance  # Update the current session balance
#                     update_user_data(account_number, new_sender_balance, users)
#                     # Update receiver user data separately to ensure consistency
#                     receiver_user, receiver_users = get_user_data(receiver_account)
#                     update_user_data(receiver_account, new_receiver_balance, receiver_users)
#                     log_activity(account_number, f'Transfer of {amount} to {receiver_account}')
#             except ValueError as ve:
#                 if 'receiver_account' in str(ve):
#                     print("Invalid input for receiver's account number. Please enter a valid numeric value.")
#                 elif 'amount' in str(ve):
#                     print("Invalid input for transfer amount. Please enter a valid numeric value.")
#                 else:
#                     print(ve)  # Print any other ValueError
#             except Exception as e:
#                 print("An unexpected error occurred:", e)
#                 continue
#         elif choice == 7:
#             account_statement(account_number)
#         else:
#             print("Invalid choice. Please enter a number between 1 and 7.")

#         another_option = input("Do you want to perform another operation? (y/n): ").strip().lower()
#         if another_option not in ('y', 'yes'):
#             print("Thanks for your patronage!")
#             ask_to_print_statement(account_number)
#             break

# def ask_to_print_statement(account_number):
#     print_statement = input("Do you want to print your account statement? (y/n): ").strip().lower()
#     if print_statement in ('y', 'yes'):
#         account_statement(account_number)

# def sign_in():
#     count = 0
#     while count < 3:
#         try:
#             account_number = int(input("Enter Account Number: "))
#             pin = int(input("Enter Account PIN: "))
#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#             continue

#         authenticated, init_balance = check_credentials(account_number, pin)
#         if authenticated:
#             print("Welcome to your account!")

#             log_activity(account_number, 'Sign in')

#             user, users = get_user_data(account_number)
#             main_menu(init_balance, account_number, users)
#             break
#         else:
#             print("<<<<<Incorrect Details>>>>")
#             count += 1

#         if count == 3:
#             print("Maximum attempts reached. Access denied.")
#             break

# if __name__ == "__main__":
#     # Check if activity log file exists, create it if not
#     if not os.path.isfile('activity_log.csv'):
#         with open('activity_log.csv', 'w', newline='') as logfile:
#             fieldnames = ['Timestamp', 'Account Number', 'Activity']
#             writer = csv.DictWriter(logfile, fieldnames=fieldnames)
#             writer.writeheader()

#     sign_in()


# import csv
# import time
# import balance
# import bills
# import deposit
# import withdrawal
# import exit
# import transfer
# import os
# from account_statement import account_statement, generate_pdf, log_activity

# def get_user_data(account_number):
#     with open('account_users.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         users = [row for row in reader]
    
#     for user in users:
#         try:
#             # Ensure the account number is valid before comparing
#             if int(user['Account Number']) == account_number:
#                 return user, users
#         except ValueError:
#             # Skip rows where Account Number is invalid or empty
#             print(f"Skipping invalid account number: {user['Account Number']}")
#             continue

#     return None, users

# def update_user_data(account_number, new_balance, users):
#     for user in users:
#         if int(user['Account Number']) == account_number:
#             user['Balance'] = str(new_balance)
#             break
#     with open('account_users.csv', 'w', newline='') as csvfile:
#         fieldnames = users[0].keys()  # dynamically fetch headers from existing data
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(users)

# def check_credentials(account_number, pin):
#     user, _ = get_user_data(account_number)
#     if user and int(user['PIN']) == pin:
#         try:
#             balance = float(user['Balance'])
#         except (ValueError, TypeError):
#             balance = 0.0
#         return True, balance
#     return False, 0.0

# def main_menu(init_balance, account_number, users):
#     while True:
#         print("1 for balance \n"
#               "2 for withdrawal \n"
#               "3 to pay bills \n"
#               "4 to deposit \n"
#               "5 to exit \n"
#               "6 to transfer \n"
#               "7 for account statement \n")
#         try:
#             choice = int(input("Choose an option: "))
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 7.")
#             continue

#         if choice == 1:
#             balance.balance(init_balance)
#             log_activity(account_number, 'Check balance')
#         elif choice == 2:
#             try:
#                 amount = float(input("Enter amount: "))
#                 if amount > init_balance:
#                     print("Insufficient funds.")
#                 else:
#                     init_balance = withdrawal.withdraw(init_balance, amount)
#                     update_user_data(account_number, init_balance, users)
#                     log_activity(account_number, f'Withdrawal of {amount}')
#             except ValueError:
#                 print("Invalid amount. Please enter a numeric value.")
#         elif choice == 3:
#             bills.bills()
#             try:
#                 bill_option = int(input("Enter bill option: "))
#                 bill_amount = float(input("Enter bill amount: "))
#                 if bill_amount > init_balance:
#                     print("Insufficient funds.")
#                 else:
#                     init_balance = bills.calc_bill(init_balance, bill_amount)
#                     update_user_data(account_number, init_balance, users)
#                     log_activity(account_number, f'Payment of bill: {bill_amount}')
#             except ValueError:
#                 print("Invalid input. Please enter numeric values.")
#         elif choice == 4:
#             try:
#                 depo = float(input("Enter deposit amount: "))
#                 init_balance = deposit.deposit(init_balance, depo)
#                 update_user_data(account_number, init_balance, users)
#                 print(f"Deposit successful. New balance: {init_balance}")
#                 log_activity(account_number, f'Deposit of {depo}')
#             except ValueError:
#                 print("Invalid amount. Please enter a numeric value.")
#         elif choice == 5:
#             update_user_data(account_number, init_balance, users)
#             log_activity(account_number, 'Exit')
#             print("Thanks for your patronage!")
#             ask_to_print_statement(account_number)
#             break
#         elif choice == 6:
#             try:
#                 receiver_account = int(input("Enter receiver's account number: "))
#                 amount = float(input("Enter amount to transfer: "))

#                 if amount > init_balance:
#                     print("Insufficient funds.")
#                 else:
#                     new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
#                     print(f"Transfer successful. New sender balance: {new_sender_balance}, New receiver balance: {new_receiver_balance}")
#                     init_balance = new_sender_balance  # Update the current session balance
#                     update_user_data(account_number, new_sender_balance, users)
#                     # Update receiver user data separately to ensure consistency
#                     receiver_user, receiver_users = get_user_data(receiver_account)
#                     update_user_data(receiver_account, new_receiver_balance, receiver_users)
#                     log_activity(account_number, f'Transfer of {amount} to {receiver_account}')
#             except ValueError as ve:
#                 if 'receiver_account' in str(ve):
#                     print("Invalid input for receiver's account number. Please enter a valid numeric value.")
#                 elif 'amount' in str(ve):
#                     print("Invalid input for transfer amount. Please enter a valid numeric value.")
#                 else:
#                     print(ve)  # Print any other ValueError
#             except Exception as e:
#                 print("An unexpected error occurred:", e)
#                 continue
#         elif choice == 7:
#             account_statement(account_number)
#         else:
#             print("Invalid choice. Please enter a number between 1 and 7.")

#         another_option = input("Do you want to perform another operation? (y/n): ").strip().lower()
#         if another_option not in ('y', 'yes'):
#             print("Thanks for your patronage!")
#             ask_to_print_statement(account_number)
#             break

# def ask_to_print_statement(account_number):
#     print_statement = input("Do you want to print your account statement? (y/n): ").strip().lower()
#     if print_statement in ('y', 'yes'):
#         account_statement(account_number)

# def sign_in():
#     count = 0
#     while count < 3:
#         try:
#             account_number = int(input("Enter Account Number: "))
#             pin = int(input("Enter Account PIN: "))
#         except ValueError:
#             print("Invalid input. Please enter numeric values.")
#             continue

#         authenticated, init_balance = check_credentials(account_number, pin)
#         if authenticated:
#             print("Welcome to your account!")

#             log_activity(account_number, 'Sign in')

#             user, users = get_user_data(account_number)
#             main_menu(init_balance, account_number, users)
#             break
#         else:
#             print("<<<<<Incorrect Details>>>>")
#             count += 1

#         if count == 3:
#             print("Maximum attempts reached. Access denied.")
#             break

# if __name__ == "__main__":
#     # Check if activity log file exists, create it if not
#     if not os.path.isfile('activity_log.csv'):
#         with open('activity_log.csv', 'w', newline='') as logfile:
#             fieldnames = ['Timestamp', 'Account Number', 'Activity']
#             writer = csv.DictWriter(logfile, fieldnames=fieldnames)
#             writer.writeheader()

#     sign_in()


import csv
import time
import balance
import bills
import deposit
import withdrawal
import exit
import transfer
import os
from account_statement import account_statement, generate_pdf, log_activity

def get_user_data(account_number):
    with open('me_info.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        users = [row for row in reader]
    
    for user in users:
        try:
            # Ensure the account number is valid before comparing
            if int(user['Account Number']) == account_number:
                return user, users
        except ValueError:
            # Skip rows where Account Number is invalid or empty
            print(f"Skipping invalid account number: {user['Account Number']}")
            continue

    return None, users

def update_user_data(account_number, new_balance, users):
    for user in users:
        if int(user['Account Number']) == account_number:
            user['Balance'] = str(new_balance)
            break
    with open('me_info.csv', 'w', newline='') as csvfile:
        fieldnames = users[0].keys()  # dynamically fetch headers from existing data
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

def check_credentials(account_number, pin):
    user, _ = get_user_data(account_number)
    if user and int(user['PIN']) == pin:
        try:
            balance = float(user['Balance'])
        except (ValueError, TypeError):
            balance = 0.0
        return True, balance
    return False, 0.0

def main_menu(init_balance, account_number, users):
    while True:
        print("1 for balance \n"
              "2 for withdrawal \n"
              "3 to pay bills \n"
              "4 to deposit \n"
              "5 to exit \n"
              "6 to transfer \n"
              "7 for account statement \n")
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            balance.balance(init_balance)
            log_activity(account_number, 'Check balance')
        elif choice == 2:
            try:
                amount = float(input("Enter amount: "))
                if amount > init_balance:
                    print("Insufficient funds.")
                else:
                    init_balance = withdrawal.withdraw(init_balance, amount)
                    update_user_data(account_number, init_balance, users)
                    log_activity(account_number, f'Withdrawal of {amount}')
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 3:
            bills.bills()
            try:
                bill_option = int(input("Enter bill option: "))
                bill_amount = float(input("Enter bill amount: "))
                if bill_amount > init_balance:
                    print("Insufficient funds.")
                else:
                    init_balance = bills.calc_bill(init_balance, bill_amount)
                    update_user_data(account_number, init_balance, users)
                    log_activity(account_number, f'Payment of bill: {bill_amount}')
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == 4:
            try:
                depo = float(input("Enter deposit amount: "))
                init_balance = deposit.deposit(init_balance, depo)
                update_user_data(account_number, init_balance, users)
                print(f"Deposit successful. New balance: {init_balance}")
                log_activity(account_number, f'Deposit of {depo}')
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == 5:
            update_user_data(account_number, init_balance, users)
            log_activity(account_number, 'Exit')
            print("Thanks for your patronage!")
            ask_to_print_statement(account_number)
            break
        elif choice == 6:
            try:
                receiver_account = int(input("Enter receiver's account number: "))
                amount = float(input("Enter amount to transfer: "))

                if amount > init_balance:
                    print("Insufficient funds.")
                else:
                    new_sender_balance, new_receiver_balance = transfer.transfer(init_balance, amount, account_number, receiver_account, update_user_data, get_user_data)
                    print(f"Transfer successful. New sender balance: {new_sender_balance}, New receiver balance: {new_receiver_balance}")
                    init_balance = new_sender_balance  # Update the current session balance
                    update_user_data(account_number, new_sender_balance, users)
                    # Update receiver user data separately to ensure consistency
                    receiver_user, receiver_users = get_user_data(receiver_account)
                    update_user_data(receiver_account, new_receiver_balance, receiver_users)
                    log_activity(account_number, f'Transfer of {amount} to {receiver_account}')
            except ValueError as ve:
                if 'receiver_account' in str(ve):
                    print("Invalid input for receiver's account number. Please enter a valid numeric value.")
                elif 'amount' in str(ve):
                    print("Invalid input for transfer amount. Please enter a valid numeric value.")
                else:
                    print(ve)  # Print any other ValueError
            except Exception as e:
                print("An unexpected error occurred:", e)
                continue
        elif choice == 7:
            account_statement(account_number)
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

        another_option = input("Do you want to perform another operation? (y/n): ").strip().lower()
        if another_option not in ('y', 'yes'):
            print("Thanks for your patronage!")
            ask_to_print_statement(account_number)
            break

def ask_to_print_statement(account_number):
    print_statement = input("Do you want to print your account statement? (y/n): ").strip().lower()
    if print_statement in ('y', 'yes'):
        account_statement(account_number)

def sign_in():
    count = 0
    while count < 3:
        try:
            account_number = int(input("Enter Account Number: "))
            pin = int(input("Enter Account PIN: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        authenticated, init_balance = check_credentials(account_number, pin)
        if authenticated:
            print("Welcome to your account!")

            log_activity(account_number, 'Sign in')

            user, users = get_user_data(account_number)
            main_menu(init_balance, account_number, users)
            break
        else:
            print("<<<<<Incorrect Details>>>>")
            count += 1

        if count == 3:
            print("Maximum attempts reached. Access denied.")
            break

if __name__ == "__main__":
    # Check if activity log file exists, create it if not
    if not os.path.isfile('activity_log.csv'):
        with open('activity_log.csv', 'w', newline='') as logfile:
            fieldnames = ['Timestamp', 'Account Number', 'Activity']
            writer = csv.DictWriter(logfile, fieldnames=fieldnames)
            writer.writeheader()

    sign_in()
