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
while option != 0:

    option = helpers.user_input()
    if option == 6:
        break
    elif option == 1:
        helpers.deposit_money(user, bank)
    elif option == 2:
        helpers.withdraw_money(user, bank)
    elif option == 3:
        helpers.update_details(user, bank)
    elif option == 4:
        helpers.check_account_balance(user, bank)
    elif option == 5:
        helpers.transaction_history(user, bank)
    else:
        print("Invalid Option")
