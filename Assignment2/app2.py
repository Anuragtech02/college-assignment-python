'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

Write a Python program to compute the sum of all the elements of each tuple
stored inside a list of tuples
Original list of tuples: [(1,2),(2,3),(3,4)]
Sum of all the elements of each tuple stored inside the said list of tuples: [3,5,7]
'''

original_tuple = [(1, 2), (2, 3), (3, 4)]
tp_sum = []


def sum_using_loop(test_tuple):
    '''
        Using loop. Iterates through all tuples inside the list and calculates sum
    '''

    for tp in test_tuple:
        total = 0
        for item in tp:
            total += item
        tp_sum.append(total)


sum_using_loop(original_tuple)


print(tp_sum)  # [3,5,7]


###################################


def sum_using_sum(test_tuple):
    '''
        Finds sum using the builtin sum function by converting tuple to list.
    '''
    for tp in test_tuple:
        tp_sum.append(sum(list(tp)))


print(tp_sum)  # [3,5,7]
