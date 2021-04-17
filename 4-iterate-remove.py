# https://thispointer.com/python-iterate-over-dictionary-and-remove-items/
# https://thispointer.com/python-remove-elements-from-a-list-while-iterating/
# https://thispointer.com/python-how-to-remove-multiple-elements-from-list/


### Issue in deleting items from dictionary while iterating [Problem]
# Dictionary changed size during iteration in python

# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Wrong way to delete an item from dictionary while iteration 
# RuntimeError: dictionary changed size during iteration
for key, value in word_freq.items():
    if value == 23:
        del word_freq[key]
print(word_freq)


# Remove key-value pairs from dictionary during Iteration [Solved]
# We can create a copy of dictionary and iterate over that and delete elements from original dictionary while iteration. For example, we have a dictionary of string and integers. We want to delete all iterate over this dictionary and delete items where value is matching a given value. Let’s see how to do that,

# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Delete an item from dictionary while iteration 
for key, value in dict(word_freq).items():  # create a word_freq copy by dict()
    if value == 23:
        del word_freq[key]
print(word_freq)


# 1. Iterate over a dictionary and remove items with even values  --- using del
# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Delete items from dictionary while iterating
# and based on conditions on values
for key, value in dict(word_freq).items():
    if value % 2 == 0:
        del word_freq[key]
print(word_freq)


# 2. Delete items from dictionary while iterating --- using comprehension

# Iterate over a dictionary and remove items with even values
# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
# Delete items from dictionary while iterating using comprehension
# and based on conditions on values
word_freq = {   key: value 
                for key, value in word_freq.items()
                if value % 2 != 0}
print(word_freq)


# 3. Iterate over a dictionary and remove items ---  using pop() function
# Dictionary of string and integers
word_freq = {
    'Hello' : 56,
    'at'    : 23,
    'test'  : 43,
    'This'  : 78,
    'Why'   : 11
}
for key in dict(word_freq):
    if word_freq[key] % 2 == 0:
        word_freq.pop(key)
print(word_freq)



#####   Python: Remove elements from a list while iterating

# 1. Remove elements from list in for loop

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]

for elem in list(list_of_num):
    if elem == 54 or elem == 55:
        list_of_num.remove(elem)
print(list_of_num)


# Why can’t we just iterate over the original list and delete elements while iterating?
# When we delete an element from a list using the remove() function in Python, it changes the remaining elements’ indexing. So if we are iterating over a list and we deleted an element from it while iterating over it, it will cause iterator invalidation and give unexpected results. Let’s understand by an example,

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
for elem in list_of_num:
    if elem == 54 or elem == 55:
        list_of_num.remove(elem)
print(list_of_num)

# output: [51, 52, 53, 55, 56, 57, 58, 59]

# In this example, we were trying to delete 54 & 55 from the list while iterating over it. When we deleted 52, it internally shifted the indexing of all the elements after 52, and our iterator becomes invalid. Due to this, during the next iteration, it picks the element after 55 and skips the 55. So 54 got deleted, but 55 was skipped.


# 2. Remove elements from a list while iterating using list comprehension
# We can iterate over the list and select elements we want to keep in the new list using list comprehension. Then we can assign the new list to the same reference variable, which was part to the original list. For example,

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove all occurrences of 54 & 55 from list
list_of_num = [num for num in list_of_num if num != 54 and num !=55 ]
print(list_of_num)

# output: [51, 52, 53, 56, 57, 58, 59]

# It created a new list, and then we assigned the new list back to the same reference variable. So it gave an effect that we have removed elements from the list while iterating over it. But internally, it created a new list.

# 3. Remove elements from a list while iterating using filter() function

# Filter() function accepts two arguments,
# First is a Lambda function or any other function
# Second is the list from which we want to delete elements

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Remove all occurrences of 54 & 55 from list
list_of_num = list(filter(lambda num: num != 54 and num !=55,
                          list_of_num)
                   )
print(list_of_num)

# output: [51, 52, 53, 56, 57, 58, 59]


#### Python : How to remove multiple elements from list ?

# Suppose we have a list of numbers i.e.
# List of Numbers
listOfnum = [12, 44, 56, 45, 34, 3, 4, 33, 44]

# 1. Remove multiple elements from list while Iterating

# Remove all numbers from list which are divisible by 3
for elem in list(listOfnum):
    if elem % 3 == 0:
        listOfnum.remove(elem)
print(listOfnum)
# output: [44, 56, 34, 4, 44]

# 2. Remove multiple elements from list using List Comprehension

# Remove all numbers from list which are divisible by 3
listOfnum = [12, 44, 56, 45, 34, 3, 4, 33, 44]
listOfnum = [ elem for elem in listOfnum if elem % 3 != 0]
print(listOfnum)


# 3. Remove Multiple elements from list by index range using del
# List of Numbers
listOfnum = [12, 44, 56, 45, 34, 3, 4, 33, 44]
# Removes elements from index 1 to 3
del listOfnum[1:4]
print(listOfnum)

