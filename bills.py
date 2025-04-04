# def bills():
#     print("choose your option \n"
#           "1 for nepa bill \n"
#           "2 for dstv")
#     return

# def nepa_bill(pick_option):
#     if pick_option == 1:
#         print("input bill amount ")

# def calc_bill(init_balance, bill_amount):
#     init_balance -= bill_amount
#     print("purchase successful")
#     print("your current balance is",init_balance)


def bills():
    print("choose your option \n"
          "1 for nepa bill \n"
          "2 for dstv")
    return

def nepa_bill(pick_option):
    if pick_option == 1:
        print("input bill amount ")

def calc_bill(init_balance, bill_amount):
    if bill_amount <= 0:
        print("Invalid bill amount.")
        return init_balance

    if bill_amount > init_balance:
        print("Insufficient funds to pay the bill.")
        return init_balance

    init_balance -= bill_amount
    print("Purchase successful")
    print("Your current balance is", init_balance)
    return init_balance
