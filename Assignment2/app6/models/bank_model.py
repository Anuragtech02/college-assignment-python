"""
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

__desc__ = "This is the model for bank object"
"""
from typing import List, Dict
from .user_model import User


class Bank:
    __users_list: List[Dict] = []

    def __init__(self):
        self.__users_list: List[Dict] = []

    def create_account(self, user: User):
        """
        Creates bank account for the user by adding \n
        bank specific details to the user object.
        """
        prev_users = self.__users_list

        # Increment acc. no. by 1 if any user present otherwise 1
        if len(prev_users) == 0:
            account_number = 1
        else:
            account_number = prev_users[-1].get("account_number") + 1

        __transaction_history: List[Dict] = []

        new_user = {
            **user.get_user(),
            "idx": len(prev_users),
            "account_number": account_number,
            "account_balance": 0,
            "transaction_history": __transaction_history,
        }
        prev_users.append(new_user)
        self.__users_list = prev_users

    def __get_current_user(self, user: User):
        """
        __requires__ = 'User object' \n
        Returns user if found in the list. Search by username
        """
        for usr in self.__users_list:
            if usr.get("username") == user.username:
                return usr
        return None

    def get_account_balance(self, user: User, pin: str):
        if not user.verify_pin(pin):
            return {"error": "Incorrect pin"}

        if not self.__get_current_user(user):
            return {"error": "User not found"}

        return self.__get_current_user(user).get("account_balance")

    def credit_money(self, user: User, amount: float):

        if(amount <=0 ):
            return {"error": "Amount must be greater than 0"}

        # Get the current user and increment amount
        curr_user = self.__get_current_user(user)
        curr_user["account_balance"] = curr_user.get("account_balance") + amount

        # Update transaction history as per the action
        history = curr_user.get("transaction_history")
        history.append({"type": "credit", "amount": amount})
        new_users_list = self.__users_list

        # Finally, get the index of current user and update users list
        new_users_list[curr_user.get("idx")] = curr_user
        self.__users_list = new_users_list

    def withdraw_money(self, user: User, amount: float):
        # Get the current user
        curr_user = self.__get_current_user(user)

        if(amount == -1):
            return

        if(amount <= 0):
            return {"error": "Amount must be greater than 0"}

        if curr_user.get("account_balance") < amount:
            return {"errror": "Not enough balance"}

        curr_user["account_balance"] = curr_user.get("account_balance") - amount

        # Update transaction history as per the action
        history = curr_user.get("transaction_history")
        history.append({"type": "debit", "amount": amount})
        new_users_list = self.__users_list

        # Finally, get the index of current user and update users list
        new_users_list[curr_user.get("idx")] = curr_user
        self.__users_list = new_users_list

    def get_transaction_history(self, user: User):
        return self.__get_current_user(user).get("transaction_history")
