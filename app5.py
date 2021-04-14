''' 
@author Anurag Pal
CSB 19C4113

Write a Python function that takes two lists and returns True if
they have atleast one common member.
'''
list1 = [2,'abc',5,6,'xyz']
list2 = [11,'abc',20,8,'phb']

# Using loop
def have_common_elements_using_loop(list1, list2):
    flag = False
    for item1 in list1:
        for item2 in list2:
            if(item1 == item2):
                flag = True
                break
    
    return flag

print(have_common_elements_using_loop(list1,list2)) # True

###################################################

# Using Set(data structure)
def have_common_elements_using_set(list1,list2):
    flag = False
    set1 = set(list1)
    set2 = set(list2)
    flag = True if set1 & set2 else False
    return flag

print(have_common_elements_using_set(list1,list2)) # True
 