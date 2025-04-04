

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

def transfer(init_balance, amount, sender_account, receiver_account, update_user_data_func):
    sender_user, users = get_user_data(sender_account)
    receiver_user, _ = get_user_data(receiver_account)

    if not sender_user:
        raise ValueError("Sender account not found.")
    if not receiver_user:
        raise ValueError("Receiver account not found.")

    if init_balance < amount:
        raise ValueError("Insufficient funds for transfer.")

    sender_balance = float(sender_user['Balance'])
    receiver_balance = float(receiver_user['Balance'])

    if sender_balance < amount:
        raise ValueError("Sender has insufficient funds for transfer.")

    sender_balance -= amount
    receiver_balance += amount

    sender_user['Balance'] = str(sender_balance)
    receiver_user['Balance'] = str(receiver_balance)

    update_user_data_func(sender_account, sender_user['Balance'], users)
    update_user_data_func(receiver_account, receiver_user['Balance'], users)

    return sender_balance, receiver_balance
