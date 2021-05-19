# https://thispointer.com/6-ways-to-get-the-last-element-of-a-list-in-python/
# https://thispointer.com/python-remove-last-element-from-a-list/
# https://thispointer.com/python-remove-first-element-from-a-list-5-ways/
# https://thispointer.com/python-remove-elements-from-list-by-value/
# https://thispointer.com/python-how-to-remove-multiple-elements-from-list/
# https://thispointer.com/python-dictionary-clear-function-examples/


### 6 ways to get the last element of a list in Python

# 1. Get last item of a list using negative indexing

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get last element by accessing element at index -1
last_elem = sample_list[-1]
print('Last Element: ', last_elem)

# 2. Get last item of a list using list.pop()

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Remove and returns the last item of list
last_elem = sample_list.pop()
print('Last Element: ', last_elem)
# now the list turned to:
print(sample_list)
print("the list size is: ", len(sample_list))
# now we clear it all:
while len(sample_list) > 0:
  sample_list.pop()

print("what is supposed to left now? ", sample_list)

# 3. Get last item of a list by slicing

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get a Slice of list, that contains only last item and select that item 
last_elem = sample_list[-1:][0]
print('Last Element: ', last_elem)


# 4. Get last item of a list using itemgetter

import operator
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
last_elem = operator.itemgetter(-1)(sample_list)
print('Last Element: ', last_elem)

# 5. Get last item of a list through Reverse Iterator

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# get Reverse Iterator and fetch first element from reverse direction
last_elem = next(reversed(sample_list), None)
print('Last Element: ', last_elem)


# Get last item of a list by indexing

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# get element at index position size-1
last_elem = sample_list[len(sample_list) - 1]
print('Last Element: ', last_elem)



### remove all elements:

list_of_num = [1, 2, 3, 4]
list_of_num.clear()
# or use del:
# del list_of_num[:]

####  Python: Remove last element from a list in 3 ways:

# 1. Remove the last element from a list in Python using the pop() function
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove last element from list
list_of_num.pop()
print(list_of_num)

# 2. Remove the last element from a list in Python using slicing
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove last element from list
list_of_num = list_of_num[:-1]
print(list_of_num)

# 3. Remove the last element from a list in Python using del keyword
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove last element from list
del list_of_num[-1]
print(list_of_num)


###  Python: Remove first element from a list (5 Ways):

# 1. Remove the first element from a list in Python using the pop() function
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove first element from list in python
list_of_num.pop(0)
print(list_of_num)

# 2. Remove the first element from a list in Python using slicing
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove first element from list in python
list_of_num = list_of_num[1:]
print(list_of_num)

# 3. Remove the first element from a list in Python using del keyword
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove first element from list in python
del list_of_num[0]
print(list_of_num)

# 4. Remove the first element from a list in Python using the remove() function
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove first element from list in python
list_of_num.remove(list_of_num[0])
print(list_of_num)

# 5. Remove the first element from the list in Python using deque
from collections import deque
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove first element from list in python
queue = deque(list_of_num)
queue.popleft()
list_of_num = list(queue)
print(list_of_num)


###   Python: Remove elements from list by value

# 1. Python: Remove the first occurrence of an element from a list by value

list_of_num = [51, 52, 53, 54, 55, 52, 57, 52, 59]
# Remove first occurrence of 52 from list
list_of_num.remove(52)
print(list_of_num)

# 2. Python: Remove element from a list by value if exist
list_of_num = [51, 52, 53, 54, 55, 52, 57, 52, 59]
elem = 70
if elem in list_of_num:  # check exist using `in`
    list_of_num.remove(elem)
print(list_of_num)


# 3. Python: Remove all occurrences of an element from a list by value
def remove_all_occurrences(list_obj, value):
    while value in list_obj:
        list_of_num.remove(value)
list_of_num = [51, 52, 52, 55, 55, 52, 57, 52, 55]
remove_all_occurrences(list_of_num, 52)
print(list_of_num)

# 4. Python: Remove all occurrences of multiple elements from a list by values
def remove_all_by_values(list_obj, values):
    for value in values:
        while value in list_obj:
            list_of_num.remove(value)
list_of_num = [51, 52, 52, 55, 55, 52, 57, 52, 55, 61, 62]
remove_all_by_values(list_of_num, [52, 55, 57])
print(list_of_num)



###   Python : How to remove multiple elements from list ?
# Python : How to remove multiple elements from list ?
# Suppose we have a list of numbers i.e.
# List of Numbers
listOfnum = [12, 44, 56, 45, 34, 3, 4, 33, 44]

# Now we want to remove all the numbers from list, which are multiple of 3.

# 1. Remove multiple elements from list while Iterating

# Remove all numbers from list which are divisible by 3
for elem in list(listOfnum):
    if elem % 3 == 0:
        listOfnum.remove(elem)

print(listOfnum)

# 2. Remove multiple elements from list using List Comprehension
# Remove all numbers from list which are divisible by 
listOfnum = [12, 44, 56, 45, 34, 3, 4, 33, 44]
listOfnum = [ elem for elem in listOfnum if elem % 3 != 0]
print(listOfnum)

# 3. Remove Multiple elements from list by index range using del
# List of Numbers
listOfnum = [12, 44, 56, 45, 34, 3, 4, 33, 44]
# Removes elements from index 1 to 3
del listOfnum[1:4]
print(listOfnum)



###  Python Dictionary: clear() function & examples

# dict.clear() Syntax:
# dict.clear()

# 1. Empty a dictionary python

# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}
print('Original Dictionary:')
print(word_freq)
# Remove all key-value pairs from the dictionary
word_freq.clear()
print('Updated Dictionary:')
print(word_freq)

# 2. Clear all dictionaries in a list of dictionaries

# List of dictionaries
list_of_dict = [
    {'Name': 'Shaun', 'Age': 35},
    {'Name': 'Ritika', 'Age': 31},
    {'Name': 'Smriti', 'Age': 33},
    {'Name': 'Jacob', 'Age': 23},
]
print('Original Dictionary:')
print(list_of_dict)
# Clear all dictionaries in a list of dictionaries
for elem in list_of_dict:
    elem.clear()
print('Updated Dictionary:')
print(list_of_dict)


