''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to count the number of strings where
the string length is 2 or more and the first and last character are
same from a given list of strings.
sample_list = ['abc','xyz','aba','1221']
'''

sample_list = ['abc','xyz','aba','1221']

count=0

for item in sample_list:
    first_char = item[0]
    last_char = item[-1]
    if((first_char == last_char) and len(item) >= 2):
        count+=1

print(count) # 2