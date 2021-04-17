# https://thispointer.com/python-check-if-dictionary-is-empty/
# https://thispointer.com/python-check-if-a-list-or-list-of-lists-is-empty-or-not/


### Python: Check if dictionary is empty

# 1. Check if a dict is empty by casting dictionary to bool in if statement

# A Dictionary of string and integers
word_freq = {
    'Hello': 56,
    "at": 23,
    'test': 43,
    'This': 78,
    'Why': 11
}
if word_freq:
    print('Dictionary is not empty')
else:
    print('Dictionary is empty')

# output: Dictionary is not empty

# An empty dictionary
sample_dict = {}
if sample_dict:
    print('Dictionary is not empty')
else:
    print('Dictionary is empty')

# output: Dictionary is empty


# 2. Check if the dictionary is empty or not using len()

# A Dictionary of string and integers
word_freq = {
    'Hello': 56,
    "at": 23,
    'test': 43,
    'This': 78,
    'Why': 11
}
if len(word_freq):
    print('Dictionary is not empty')
else:
    print('Dictionary is empty')

# output: Dictionary is not empty

# An empty dictionary
sample_dict = {}
if len(sample_dict):
    print('Dictionary is not empty')
else:
    print('Dictionary is empty')

# output: Dictionary is empty




####   Python: Check if a list is empty or not – ( Updated 2020 )


# 1. Check if a list is empty using ‘not’ operator in python

# Create an empty list
list_of_num = []
# Empty list object will evaluate to False
if not list_of_num:
    print('List is empty')
else:
    print('List is not empty')

# output: List is empty

# 2. Check if list is empty using len() function

# Create an empty list
list_of_num = []
# Check if list's size is 0
if len(list_of_num) == 0:
    print('List is empty')
else:
    print('List is not empty')

# output: List is empty

# 3. Python: Check if list is empty by comparing with empty list

# Create an empty list
list_of_num = []
# Check if list object points to literal []
if list_of_num == []:
    print('List is empty')
else:
    print('List is not empty')

# output: List is empty


# 4. Check if list is empty using __len__()

# Create an empty list
list_of_num = []
# Check if list's size is 0
if list_of_num.__len__() == 0:
    print('List is empty')
else:
    print('List is not empty')

# output: List is empty







