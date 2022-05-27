# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count

def read_file_content(filename):
    # [assignment] Add your code here 

    # open, read & close
    open_file = open(filename, "r")
    read_file = open_file.read()
    open_file.close()
    return read_file
    # return "Hello World"


# count fn_
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    # empty dict. for storage 
    count_and_store_in = dict()
    # remove excess space
    strip_text = text.strip()
    # create word seperator
    split_text = strip_text.split()
 
    for a_particular_word in split_text:
        if a_particular_word not in count_and_store_in:
            count_and_store_in[a_particular_word] = 1    
        else:
           count_and_store_in[a_particular_word] += 1  
    return count_and_store_in
    # # return {"as": 10, "would": 20}

print(count_words())
