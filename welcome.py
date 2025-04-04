
from outer import sign_in
from creater import create_user
import csv

def welcome():
    print("===================================")
    print("   Welcome to Our Banking System   ")
    print("===================================")
    print("Please follow the instructions.")
    print("1. Create Account\n2. Sign in")
    
    try:
        option = int(input("Kindly input option: "))
        if option == 1:
            create_user()
            welcome()
        elif option == 2:
            sign_in()
        else:
            print("Invalid option. Please choose 1 or 2.")
            welcome()
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        welcome()
welcome()
