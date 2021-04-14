''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to check whether a list contains a sublist.
'''

sample_list = [1, 2, 3, 4, 5, 6]

def contains_sub_list(lst, sub_list):
    flag = True
    for item in sub_list:
        if item not in lst: flag = False
    return flag

print(contains_sub_list(sample_list,[2,3,4]))