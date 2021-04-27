''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to flatten a multi-dimensional list.
'''

sample_list = [1, [2, 3, 4], 5, 6]

# Using loops
def flatten_list(lst):
    temp_list = []
    for item in lst:
        # Check if the item is a list 
        if(type(item) == type([])):
            for inner_item in item:
                temp_list.append(inner_item)
        else: temp_list.append(item)

    return temp_list

print(flatten_list(sample_list)) # [1, 2, 3, 4, 5, 6]

#################################

# Using sum function
# This works only if the items in the list are also lists
sample_list2 = [[1,2,3,],[4,5,6,]]
print(sum(sample_list2,[])) # [1, 2, 3, 4, 5, 6]