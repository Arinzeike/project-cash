
import balance
import withdrawal
import deposit
import bills
import exit

pass
initial_balance = 10
a = 0
while a != 3:


    pin = int(input("please enter your pin: "))
    if pin == pin:
        print("welcome UBA")
        print("1 for balance \n"
              "2 for withdrawal \n"
              "3 pay bills \n"
              "4 deposit \n"
              "5 exit")
        break
    else:
        print("invalid pin")

    retry_pin = input("do you want to try again (Y or N)".lower())

    if retry_pin == "yes" or "y":


        if a == 0:
            print("you have 2 trials left")

        if a == 1:
            print("you have 1 trial left")

        if a == 2:
            print("you have been blocked")
        break

a = a + 1

b = "yes" or "y"
while b == "yes" or "y":
# stage 2 menu
    choice = int(input("choose option: "))
# call balance function
    if choice == 1:
        balance.balance(initial_balance)
# call withdrawal function
    if choice == 2:
        amount = int(input("enter amount: "))
        if amount > initial_balance:
            print("insufficient fund")
        else:
            initial_balance = withdrawal.withdraw(initial_balance,amount)
# call deposit function
    if choice == 4:
        depo = int(input("enter deposit amount: "))
        initial_balance = deposit.deposit(initial_balance,depo)
# call bill function
    if choice == 3:
        bills.bills()
        bill_option = int(input("enter option: "))
        bill_amount = int(input("enter bill amount"))
        if bill_amount > initial_balance:
            print("insufficient funds")
        else:

            bills.calc_bill(initial_balance,bill_amount)

    if choice >= 5 :
        exit.exitapp()


    b = input("do you want to perform another transaction ".lower())
    if b == "yes" or "y":

        print("1 for balance \n"
                  "2 for withdrawal \n"
                  "3 pay bills \n"
                  "4 deposit \n"
                  "5 exit")


