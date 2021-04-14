''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to remove duplicates from a list.
'''
sample_list = ['abc','xyz','aba','1221', 'aba', 'xyz', 'some random string']

temp = []
for item in sample_list:
    if item not in temp:
        temp.append(item)

print(temp) # ['abc', 'xyz', 'aba', '1221', 'some random string']
