''' 
@author Anurag Pal
CSB 19C4113

Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black","Red","Maroon","Yellow"],["#000000", "#FF0000","#800000","#FFFF00"]
Expected Output: [{'color_name':'Black','color_code':'#000000'},
{'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name':
'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow',
'color_code':'#FFFF00'}
'''

labels = ["Black","Red","Maroon","Yellow"]
hex_codes = ["#000000", "#FF0000","#800000","#FFFF00"]

output = []

for i in range(len(labels)-1):
    label = labels[i]
    hex_code = hex_codes[i]
    output.append({'color_name':label, 'color_code': hex_code})

print(output)