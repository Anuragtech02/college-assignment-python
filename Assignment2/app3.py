'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

In this problem, we need to extract all possible unique combination of 2
argument tuples
Input: test_tuple1=(7,2),test_tuple2=(7,8)
Output: [(7,7),(7,8),(2,7),(2,8),(7,2),(8,7),(8,2)]
'''

test_tuple1 = (7, 2)
test_tuple2 = (7, 8)


def combinations_using_loop(tuple1, tuple2):
    '''
        Iterates through tuples twice keeping in mind to include only unique values
    '''
    res = []
    for tp1 in tuple1:
        for tp2 in tuple2:
            if((tp1, tp2) not in res):
                res.append((tp1, tp2))

    # interchanged tuple1 and tuple2
    for tp1 in tuple2:
        for tp2 in tuple1:
            if((tp1, tp2) not in res):
                res.append((tp1, tp2))

    return res


print(combinations_using_loop(test_tuple1, test_tuple2))
# [(7,7),(7,8),(2,7),(2,8),(7,2),(8,7),(8,2)]
