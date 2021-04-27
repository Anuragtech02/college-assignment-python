'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

__desc__ = "This is the schema/model for bank object"
'''
from typing import List,Dict
from user_model import User

class Bank:

    def __init__(self, user:User):
        self.__account_number:str = None
        self.__account_balance:float = 0
        self.user=user
        self.__transaction_history:List[Dict] = []

    


        
