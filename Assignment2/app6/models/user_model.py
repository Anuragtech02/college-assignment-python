"""
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

__desc__ = "This is the schema/model for user object"
"""

from pydantic import (
    BaseModel,
)  # Python base models. Parent class of all data types in python


class User:
    def __init__(self, name: str, mobile: str, pin: str, username: str, password: str):
        self.name: str = name
        self.mobile: str = mobile
        self.__pin: str = pin
        self.username: str = username
        self.__password: str = password
        

    def verify_user(self, uname, passd):
        return self.username == uname and self.__password == passd

    def verify_pin(self, pin):
        return self.__pin == pin

    def get_user(self):
        return {"name": self.name, "mobile": self.mobile, "username": self.username}

    def __modify_name(self, new_name):
        self.name = new_name

    def __modify_mobile(self, new_mobile):
        self.mobile = new_mobile

    @property
    def __modify_pin(self, new_pin):
        self.__pin = new_pin

    @property
    def __modify_pass(self, new_pass):
        self.__password = new_pass

    @property
    def __modify_private(self, ctype, cpass, value):
        if cpass != self.__password:
            return {"error": "incorrect password"}
        if ctype == "password":
            self.__modify_pass = value
        elif ctype == "pin":
            self.__modify_pin = value

    def modify_user(self, ctype, value):
        if ctype == "name":
            self.__modify_name(value)
        elif ctype == "mobile":
            self.__modify_mobile(value)
        elif ctype == "password" or ctype == "pin":
            self.__modify_private(ctype, value.get("cpass"), value.get(ctype))
