#! /usr/bin/env python
#You are allowed only to create new lines, 
#not to delete or change the lines already in the code

# Author: Branden Kim
# 3b

def replace_characters(string, a, b):
    new_word = ""
    i=0
    while i<len(string):
        if string[i] == a:
            new_word += b
        else:
            new_word += string[i]
        i = i+1
        
    return new_word
    
print(replace_characters("word", "o", "A"))