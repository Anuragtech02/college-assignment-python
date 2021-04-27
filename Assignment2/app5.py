'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

Given the following dictionary:
    inventory={
    'gold':500,
    'pouch':['flint','twine','gemstone'],
    'backpack':['xylophone','dagger','bedroll','breadloaf']
    }
Flatten it all in to a single list:
Output: ['gold'',500,'pouch','flint','twine','gemstone','backpack','xylophone','dagger',
'bedroll','breadloaf']
'''

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'breadloaf']
}


def flatten_dict(dict):
    '''
        For Python version < 3.7, the order of items in a dictionary is reversed. The function 
        reversed is being used to maintain the order
    '''
    res = []
    # reversed() should be omitted for python version >=3.7
    for key, value in reversed(dict.items()):
        res.append(key)
        if type(value) == type([]):
            res.extend(value)
        else:
            res.append(value)
    return res


print(flatten_dict(inventory))
# ['gold', 500, 'pouch', 'flint', 'twine', 'gemstone', 'backpack', 'xylophone', 'dagger', 'bedroll', 'breadloaf']
