'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

Write a Python program to check if a specified element presents in a tuple of
tuples.
Originallist:(('Red','White','Blue'),('Green','Pink','Purple'),('Orange','Yellow',
'Lime'))
'''

original_tuple = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow',
                                                                          'Lime'))

element_to_check = "Blue"

# Using loop


def is_element_present(element):
    '''
        Using loop. Iterates through all the elements and checks if the asked element is present
    '''

    for tp in original_tuple:
        if(element in tp):
            return True
    return False


print(is_element_present(element_to_check))
