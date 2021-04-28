"""
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

__desc__ = "Utility/Helper functions for main"
"""

import getpass  # Used to hide password on terminal


def print_options():
    """
    Prints possible menu options to the user
    """
    print("*" * 30)
    print(
        "Please select the action you want to perform (option number): ",
        "1. Deposit Money",
        "2. Withdraw Money",
        "3. Update Details",
        "4. Check Account Balance",
        "5. View Transaction History",
        "6. Exit",
        sep="\n",
    )


def user_input():
    """
    Prints menu and asks for option input to the user
    """
    print_options()
    print("*" * 30)
    option = int(input())
    return option


def create_bank_account():
    """
    Takes all input details from the user, requried for creating bank account.
    """
    print("*" * 30)
    name = input("Enter your name: ")
    username = input("Create an username: ")
    mobile = input("Enter your mobile number: ")
    password = getpass.getpass(prompt="Create a password: ")
    while len(password) < 8:
        print("Password must be of at least 8 digits")
        password = getpass.getpass(prompt="Renter password: ")
    pin = getpass.getpass(prompt="Create a pin (4 digits): ")
    while len(pin) != 4:
        print("Pin must be of 4 digits")
        pin = getpass.getpass(prompt="Renter pin (4 digits) ")
    return {
        "name": name,
        "username": username,
        "mobile": mobile,
        "password": password,
        "pin": pin,
    }
