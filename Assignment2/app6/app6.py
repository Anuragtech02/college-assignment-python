"""
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

Use OOPS concept and replicate the functioning of a Bank.
Bank gives us whatever facilities, create a programming model that is generic
enough to give output with certain inouts by the user. If possible, explain the
objects as sumed by you and the functions defined.
"""

"""
    Bank facilities assumed
    1. Create Bank Account
    2. Deposit Money
    3. Withdraw Money
    4. Update Details
    5. Check Account Balance
    6. View Transaction History
"""

from models import User, Bank
import helpers
import getpass

bank = Bank()

print(
    "Hey, Welcome to the bank!",
    "Please fill some details to create your bank account: ",
    sep="\n",
)
input_data = helpers.create_bank_account()

print("*" * 30, "Succesfully created account :)", sep="\n")

# Create new user instance using data received from input_data
user = User(
    input_data.get("name"),
    input_data.get("mobile"),
    input_data.get("pin"),
    input_data.get("username"),
    input_data.get("password"),
)

# Create bank account using user details
bank.create_account(user)

# Display menu of options available/provided by bank to the user until 0
option = None
while(option != 0):

    option = helpers.user_input()
    if(option == 6):
        break
    elif(option == 1):
        print("*"*30)
        amt = float(input("Please enter amount to depost: "))
        bank.credit_money(user, amt)
        print("*"*30, "Successfull", sep="\n")
    elif(option == 2):
        print("*"*30)
        amt = float(input("Please enter amount to withdraw: "))
        bank.withdraw_money(user, amt)
        print("*"*30, "Successfull", sep="\n")
    elif(option == 3):
        print("*"*30, "Please choose what you want to update: ", "1. Name", "2. Mobile", "3. Password", "4. PIN", sep="\n")
        choose = input()
        if(choose == 1):
            name = input("Please enter new name: ")
            user.modify_user("name", name)
            print("*"*30, "Successfull", sep="\n")
        elif(choose == 2):
            mob = input("Please enter new mobile number: ")
            user.modify_user("mobile", mob)
            print("*"*30, "Successfull", sep="\n")
        elif(choose == 3):
            curr_pwd = getpass.getpass(prompt="Please enter current password: ")
            new_pwd = getpass.getpass(prompt="Please enter new password: ")
            res = user.modify_user("password", curr_pwd, new_pwd)
            while(isinstance(res, type({}))):
                print(res)
                curr_pwd = curr_pwd = getpass.getpass(prompt="Please enter current password: ")
                new_pwd = getpass.getpass(prompt="Please enter new password: ")
                res = user.modify_user("password", curr_pwd, new_pwd)
            print("*"*30, "Successfull", sep="\n")
        elif(choose == 4):
            curr_pwd = getpass.getpass(prompt="Please enter current password: ")
            new_pwd = getpass.getpass(prompt="Please enter new PIN: ")
            res = user.modify_user("pin", curr_pwd, new_pwd)
            while(isinstance(res, type({}))):
                print(res)
                curr_pwd = curr_pwd = getpass.getpass(prompt="Please enter current password: ")
                new_pwd = getpass.getpass(prompt="Please enter new PIN: ")
                res = user.modify_user("pin", curr_pwd, new_pwd)
            print("*"*30, "Successfull", sep="\n")
        else:
            print("Invalid option")
    elif(option == 4):
        pin = input("Please enter your 4 digit PIN: ")
        res = bank.get_account_balance(user,pin)
        while(isinstance(res, type({}))):
            print(res)
            res = bank.get_account_balance(user,pin)
            print("Renter PIN: ")
        print(res)
    elif(option == 5):
        res = bank.get_transaction_history(user)
        print("*"*30)
        for transaction in res:
            print(transaction.get("type"), transaction.get("amount"), sep=" ")
    else:
        print("Invalid Option")
