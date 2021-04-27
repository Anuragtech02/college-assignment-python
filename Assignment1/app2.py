'''
@author Anurag Pal
CSB 19C4113

Write a Python program to get the largest number from a list.
'''

some_list = [10,5,1,12,8]

## Using max function
print(max(some_list)) # 12

#####################

## Using loop
largest=some_list[0]
for item in some_list:
    if item > largest:
        largest = item

print(largest) # 12