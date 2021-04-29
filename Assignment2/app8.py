'''
__author__ = "Anurag Pal"
__email__ = "19bcs113@ietdavv.edu.in"
__roll__ = "19C4113"
__class__ = "CSB"

Count frequency of each word and store into a dictionary.
Further, write the data to txt file.
'''

def get_words_with_count(file_path:str):
    
    test_file = open(file_path, "r") # Open the file in read mode
    res = {}

    for txt in test_file.read().replace("\n", " ").split(" "):
        res[txt.lower()] = (res.get(txt.lower()) or 0) + 1

    test_file.close()
    
    return res

def save_file(content:dict, output_path:str):

    try:
        output_file = open(output_path, 'wt') # Open the file in write mode
        output_file.write(str(content))
        output_file.close()
    
    except:
        print("Some error occured")

save_file(get_words_with_count("./io.txt"), "output.txt")




