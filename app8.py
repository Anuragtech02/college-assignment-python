''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to get the frequency of the elements in a
list,thereby generating a dictionary.
Sample List: [1,2,1,1,1,'abs','a',0.4,1,2,5,32,27,2,7,1,'c']
Expected Result: {1:6, 2:3, ’abs’:1, ’a’:1....}
'''

sample_list = [1,2,1,1,1,'abs','a',0.4,1,2,5,32,27,2,7,1,'c']

output = {}

for item in sample_list:
    output[item] = sample_list.count(item)

print(output) # [1,2,1,1,1,'abs','a',0.4,1,2,5,32,27,2,7,1,'c']