def deposit(init_balance,depo_amount):
    init_balance += depo_amount
    print(f"deposit of  {depo_amount} successful")
    print("your current balance is ", init_balance)
    return init_balance