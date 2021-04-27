'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

We need to remove duplicate records from a given tuple of lists.
(Make sure the order of occurence should not change)
Input:([4,7,8],[1,2,3],[4,7,8],[9,10,11],[1,2,3])
Output:([4,7,8],[1,2,3],[9,10,11])
'''

original_tuple = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])


def remove_duplicates_loop(test_tuple):
    '''
        Iterates through test_tuple returning only unique values
    '''
    res = []
    for ls in test_tuple:
        if(ls not in res):
            res.append(ls)

    return tuple(res)


print(remove_duplicates_loop(original_tuple))
# ([4, 7, 8], [1, 2, 3], [9, 10, 11])


##########################################

def remove_duplicates_map(test_tuple):
    '''
        Uses map and lambda to return tuple in single line
    '''
    return tuple(map(lambda lst: lst not in test_tuple, list(test_tuple)))


print(remove_duplicates_loop(original_tuple))
# ([4, 7, 8], [1, 2, 3], [9, 10, 11])
