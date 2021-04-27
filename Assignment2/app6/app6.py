'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

Use OOPS concept and replicate the functioning of a Bank.
Bank gives us whatever facilities, create a programming model that is generic
enough to give output with certain inouts by the user. If possible, explain the
objects as sumed by you and the functions defined.
'''

'''
    Bank facilities assumed
    1. Create Bank Account
    2. Deposit Money
    3. Withdraw Money
    4. Update Deatails
    5. Check Account Balance
    6. View Transaction History
'''

from models import User

user = User("anurag","gf",546,"sdf","sdf")

print(user.get_user())