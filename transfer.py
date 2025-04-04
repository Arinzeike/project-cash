# def transfer(init_balance,with_amount):
#     init_balance -= with_amount
#     print("your new balance is ", init_balance)
#     return init_balance
# def transfer(init_balance, amount, sender_account, receiver_account):
#     if init_balance < amount:
#         raise ValueError("Insufficient funds for transfer.")

#     sender_user, users = get_user_data(sender_account)
#     receiver_user, _ = get_user_data(receiver_account)

#     if not receiver_user:
#         raise ValueError("Receiver account not found.")

#     # Deduct the amount from sender's balance
#     sender_user['Balance'] = str(float(sender_user['Balance']) - amount)
#     # Add the amount to receiver's balance
#     receiver_user['Balance'] = str(float(receiver_user['Balance']) + amount)

#     # Update user data in the file
#     update_user_data(sender_account, sender_user['Balance'], users)
#     update_user_data(receiver_account, receiver_user['Balance'], users)

#     return float(sender_user['Balance'])
# def transfer(init_balance, amount, sender_account, receiver_account, get_user_data_func):
#     sender_user, users = get_user_data_func(sender_account)
#     receiver_user, _ = get_user_data_func(receiver_account)

#     if not sender_user:
#         raise ValueError("Sender account not found.")
#     if not receiver_user:
#         raise ValueError("Receiver account not found.")

#     if init_balance < amount:
#         raise ValueError("Insufficient funds for transfer.")

#     # Deduct the amount from sender's balance
#     sender_user['Balance'] = str(float(sender_user['Balance']) - amount)
#     # Add the amount to receiver's balance
#     receiver_user['Balance'] = str(float(receiver_user['Balance']) + amount)

#     # Update user data in the file
#     update_user_data(sender_account, sender_user['Balance'], users)
#     update_user_data(receiver_account, receiver_user['Balance'], users)

#     return float(sender_user['Balance'])
def get_user_data(account):
    # Placeholder implementation to retrieve user data based on the account identifier
    # This function interacts with a database or data storage mechanism in a real-world scenario
    users = {
        'sender_account': {'Balance': '100'},  # Example sender user data
        'receiver_account': {'Balance': '50'}  # Example receiver user data
    }

    # Retrieve user data based on the account identifier
    user_data = users.get(account)

    # Return the user data along with other related data (if any)
    return user_data, users

# def transfer(init_balance, amount, sender_account, receiver_account, update_user_data_func):
#     sender_user, users = get_user_data(sender_account)
#     receiver_user, _ = get_user_data(receiver_account)

#     if not sender_user:
#         raise ValueError("Sender account not found.")
#     if not receiver_user:
#         raise ValueError("Receiver account not found.")

#     if init_balance < amount:
#         raise ValueError("Insufficient funds for transfer.")

#     sender_balance = float(sender_user['Balance'])
#     receiver_balance = float(receiver_user['Balance'])

#     if sender_balance < amount:
#         raise ValueError("Sender has insufficient funds for transfer.")

#     sender_balance -= amount
#     receiver_balance += amount

#     sender_user['Balance'] = str(sender_balance)
#     receiver_user['Balance'] = str(receiver_balance)

#     update_user_data_func(sender_account, sender_user['Balance'], users)
#     update_user_data_func(receiver_account, receiver_user['Balance'], users)

#     return sender_balance, receiver_balance

# def transfer(init_balance, amount, sender_account, receiver_account, update_user_data_func):
#     sender_user, users = get_user_data(sender_account)
#     receiver_user, _ = get_user_data(receiver_account)

#     if not sender_user:
#         raise ValueError("Sender account not found.")
#     if not receiver_user:
#         raise ValueError("Receiver account not found.")

#     if init_balance < amount:
#         raise ValueError("Insufficient funds for transfer.")

#     sender_user['Balance'] = str(float(sender_user['Balance']) - amount)
#     receiver_user['Balance'] = str(float(receiver_user['Balance']) + amount)

#     update_user_data_func(sender_account, sender_user['Balance'], users)
#     update_user_data_func(receiver_account, receiver_user['Balance'], users)

#     return float(sender_user['Balance']), float(receiver_user['Balance'])
# 
# IT IS WORKING
# def transfer(init_balance, amount, sender_account, receiver_account, update_user_data_func, get_user_data_func):
    # Fetch sender and receiver user data
    sender_user, users = get_user_data_func(sender_account)
    receiver_user, _ = get_user_data_func(receiver_account)

    if not sender_user:
        raise ValueError("Sender account not found.")
    if not receiver_user:
        raise ValueError("Receiver account not found.")

    # Check if sender has sufficient funds
    sender_balance = float(sender_user['Balance'])
    if sender_balance < amount:
        raise ValueError("Insufficient funds for transfer.")

    # Update balances
    sender_user['Balance'] = str(sender_balance - amount)
    receiver_user['Balance'] = str(float(receiver_user['Balance']) + amount)

    # Debug print to trace the balance updates
    # print(f"Sender new balance: {sender_user['Balance']}")
    # print(f"Receiver new balance: {receiver_user['Balance']}")

    # Update both users' data
    update_user_data_func(sender_account, sender_user['Balance'], users)
    update_user_data_func(receiver_account, receiver_user['Balance'], users)

    return float(sender_user['Balance']), float(receiver_user['Balance'])
def transfer(init_balance, amount, sender_account, receiver_account, update_user_data_func, get_user_data_func):
    # Fetch sender and receiver user data
    sender_user, users = get_user_data_func(sender_account)
    receiver_user, receiver_users = get_user_data_func(receiver_account)

    if not sender_user:
        raise ValueError("Sender account not found.")
    if not receiver_user:
        raise ValueError("Receiver account not found.")

    # Check if sender has sufficient funds
    sender_balance = float(sender_user['Balance'])
    if sender_balance < amount:
        raise ValueError("Insufficient funds for transfer.")

    # Update balances
    sender_user['Balance'] = str(sender_balance - amount)
    receiver_user['Balance'] = str(float(receiver_user['Balance']) + amount)

    # Update both users' data
    update_user_data_func(sender_account, sender_user['Balance'], users)
    update_user_data_func(receiver_account, receiver_user['Balance'], receiver_users)

    return float(sender_user['Balance']), float(receiver_user['Balance'])
