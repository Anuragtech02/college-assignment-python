"""
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

__desc__ = "Utility functions for menu"
"""

from models import Bank, User
import getpass  # Used to hide password on terminal


def deposit_money(user: User, bank: Bank):
    """
    Helper function to deposit money to bank. \n
    __uses__ = bank.credit_money()
    """
    print("*" * 30)
    amt = float(input("Please enter amount to deposit: "))
    res = bank.credit_money(user, amt)
    while isinstance(res, dict):
        print(res)
        amt = float(input("Please enter amount to depost: "))
        res = bank.credit_money(user, amt)
    print("*" * 30, "Successfull", sep="\n")


def withdraw_money(user: User, bank: Bank):
    """
    Helper function to withdraw money from bank. \n
    __uses__ = bank.withdraw_money()
    """
    print("*" * 30)
    amt = float(input("Please enter amount to withdraw: "))
    res = bank.withdraw_money(user, amt)
    while isinstance(res, dict):
        print(res)
        amt = float(input("Please enter amount to withdraw: "))
        res = bank.withdraw_money(user, amt)
    print("*" * 30, "Successfull", sep="\n")


def update_details(user: User, bank: Bank):
    """
    Helper function to update user details.
    __uses__ = user.modify_user(). \n
    Updates possible: Name, Mobile, Password, PIN
    """
    print(
        "*" * 30,
        "Please choose what you want to update: ",
        "1. Name",
        "2. Mobile",
        "3. Password",
        "4. PIN",
        sep="\n",
    )
    choose = int(input())
    if choose == 1:
        name = input("Please enter new name: ")
        user.modify_user("name", name)
        print("*" * 30, "Successfull", sep="\n")
    elif choose == 2:
        mob = input("Please enter new mobile number: ")
        user.modify_user("mobile", mob)
        print("*" * 30, "Successfull", sep="\n")
    elif choose == 3:
        curr_pwd = getpass.getpass(prompt="Please enter current password: ")
        new_pwd = getpass.getpass(prompt="Please enter new password: ")
        res = user.modify_user("password", {"cpass": curr_pwd, "password": new_pwd})
        while isinstance(res, dict):
            print(res)
            curr_pwd = curr_pwd = getpass.getpass(
                prompt="Please enter current password: "
            )
            new_pwd = getpass.getpass(prompt="Please enter new password: ")
            res = user.modify_user("password", {"cpass": curr_pwd, "password": new_pwd})
        print("*" * 30, "Successfull", sep="\n")
    elif choose == 4:
        curr_pwd = getpass.getpass(prompt="Please enter current password: ")
        new_pin = getpass.getpass(prompt="Please enter new PIN: ")
        res = user.modify_user("pin", {"cpass": curr_pwd, "pin": new_pin})
        while isinstance(res, dict):
            print(res)
            curr_pwd = curr_pwd = getpass.getpass(
                prompt="Please enter current password: "
            )
            new_pin = getpass.getpass(prompt="Please enter new PIN: ")
            res = user.modify_user("pin", {"cpass": curr_pwd, "pin": new_pin})
        print("*" * 30, "Successfull", sep="\n")
    else:
        print("Invalid option")


def check_account_balance(user: User, bank: Bank):
    """
    Helper function to check account balance. \n
    __uses__ = bank.get_account_balance(). \n
    __requires__= pin
    """

    pin = getpass.getpass("Please enter your 4 digit PIN: ")
    res = bank.get_account_balance(user, pin)
    while isinstance(res, dict):
        print(res)
        pin = getpass.getpass("Renter PIN: ")
        res = bank.get_account_balance(user, pin)
    print(res)
    return res


def transaction_history(user: User, bank: Bank):
    """
    Helper function to check transaction history. \n
    __uses__ = [bank.get_account_balance(), bank.get_transaction_history()] \n
    __requires__= pin
    """

    pin = getpass.getpass("Please enter your 4 digit PIN: ")
    bal = bank.get_account_balance(user, pin)
    while isinstance(bal, dict):
        print(bal)
        pin = getpass.getpass("Renter PIN: ")
        bal = bank.get_account_balance(user, pin)

    res = bank.get_transaction_history(user)
    print("*" * 30)

    if len(res) == 0:
        print("No history found")

    for transaction in res:
        print(transaction.get("type").upper(), transaction.get("amount"), sep=" ")

    print("-" * 20)
    print("CURR BAL.", bal)
