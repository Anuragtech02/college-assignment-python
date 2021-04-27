''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to generate all permutations of a list in
Python.
'''

sample_list = [1,2,3]

# Using the permutations function
from itertools import permutations
print(list(permutations(sample_list))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

#####################################

# Using Recursion
def permutations(lst):

    # Check for empty input list
    if not len(lst): return [];

    # If list has only one item
    if len(lst) == 1: return [lst]

    temp_list = []

    for i in range(len(lst)):

        # Take the current element fixed
        m = lst[i]

        remaining = lst[:i] + lst[i+1:]

        # Iterate through all the remainng items in the list (recursively)
        for item in permutations(remaining):
            temp_list.append([m] + item)
    
    return temp_list

print(permutations(sample_list)) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]



