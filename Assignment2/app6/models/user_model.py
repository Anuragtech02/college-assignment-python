"""
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

__desc__ = "This is the model for user object"
"""


class User:
    def __init__(self, name: str, mobile: str, pin: str, username: str, password: str):
        self.name: str = name
        self.mobile: str = mobile
        self.__pin: str = pin
        self.username: str = username
        self.__password: str = password

    def verify_user(self, uname, passd):
        """
        Check if username and password match
        """
        return self.username == uname and self.__password == passd

    def verify_pin(self, pin):
        return self.__pin == pin

    def get_user(self):
        return {"name": self.name, "mobile": self.mobile, "username": self.username}

    def __modify_name(self, new_name):
        self.name = new_name

    def __modify_mobile(self, new_mobile):
        self.mobile = new_mobile

    def __modify_pin(self, new_pin):
        self.__pin = new_pin

    def __modify_pass(self, new_pass):
        self.__password = new_pass

    def __modify_private(self, ctype: str, value: dict):
        if value.get("cpass") != self.__password:
            return {"error": "incorrect password"}
        if ctype == "password":
            self.__modify_pass(value.get(ctype))
        elif ctype == "pin":
            self.__modify_pin(value.get(ctype))

    def modify_user(self, ctype: str, value):
        """
        Modifies user data. \n
        __requires__ = '[ctype: Change Type, value: str | dict]' \n
        The parameter value is assumed to be a dict if ctype is password or pin
        """
        if ctype == "name":
            self.__modify_name(value)
        elif ctype == "mobile":
            self.__modify_mobile(value)
        elif ctype == "password" or ctype == "pin":
            self.__modify_private(ctype, value)
