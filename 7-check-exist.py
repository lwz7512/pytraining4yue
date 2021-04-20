# https://thispointer.com/python-check-if-a-value-exists-in-the-dictionary-3-ways/
# https://thispointer.com/python-how-to-check-if-a-key-exists-in-dictionary/



# Python: check if key exists in dictionary (6 Ways)


# Suppose we have a dictionary of string and int i.e.

# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}

################
# Now we want to check if key ‘test’ exist in this dictionary or not.
################

# 1. Python: check if key in dictionary using if-in statement


key = 'test'
# python check if key in dict using "in"
if key in word_freq:
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")


# output: Yes, key: 'test' exists in dictionary


key = 'sample'
# python check if key in dict using "in"
if key in word_freq:
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# output: No, key: 'sample' does not exists in dictionary


# 2. Python: check if dict has key using get() function

# In python, the dict class provides a method get() that accepts a key and a default value i.e.
# dict.get(key[, default])

# Behavior of this function,
# If given key exists in the dictionary, then it returns the value associated with this key,
# If given key does not exists in dictionary, then it returns the passed default value argument.
# If given key does not exists in dictionary and Default value is also not provided, then it returns None.


key = 'sample'
# check if key exists in dictionary by checking if get() returned None
if word_freq.get(key) is not None:
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# No, key: 'sample' does not exists in dictionary


# check if key exists in dictionary by checking if get() returned default value
if word_freq.get(key, -1) != -1:
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# output: No, key: 'sample' does not exists in dictionary


# 3. Python: check if key in dict using keys()

key = 'test'
if key in word_freq.keys():
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# output: Yes, key: 'test' exists in dictionary


# 4. python check if key in dictionary using try/except

def check_key_exist(test_dict, key):
    try:
       value = test_dict[key]
       return True
    except KeyError:
        return False
# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}
key = 'test'
# check if dictionary has key in python
if check_key_exist(word_freq, key):
    print(f"Yes, key: '{key}' exists in dictionary")
else:
    print(f"No, key: '{key}' does not exists in dictionary")

# output: Yes, key: 'test' exists in dictionary


# 5. Check if key not in dictionary in python using ‘if not in’ statement

word_freq = { "Hello": 56, "at": 23, "test": 43, "this": 78 }
key = 'sample'
# Check if key not in dict python
if key not in word_freq:
    print(f"No, key: '{key}' does not exists in dictionary")
else:
    print(f"Yes, key: '{key}' exists in dictionary")

# output: No, key: 'sample' does not exists in dictionary


# 6. Check if key exist in dictionary using has_key() function

if word_freq.has_key('test'):
    print("Yes 'test' key exists in dict")
else:
    print("No 'test' key does not exists in dict")

# output: Yes, key: 'test' exists in dictionary



















### Python: Check if a value exists in the dictionary (3 Ways)
# 
# Check if value exist in a dict using values() & if-in statement
# Check if a value exists in python dictionary using for loop
# Check if a value exists in a dictionary using any() and List comprehension
#  

# Suppose we have a dictionary of strings and ints i.e.
# Dictionary of string and int
word_freq = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 78
}
# Now in this dictionary we want to check if any key contains the value 43 or not 

# 1. Check if value exist in dict using values() & if-in statement

value = 43
# python check if value exist in dict using "in" & values()
if value in word_freq.values():
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")


value = 51
# python check if value exist in dict using "in" & values()
if value in word_freq.values():
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")

# 2. Check if a value exists in python dictionary using for loop

def check_value_exist(test_dict, value):
    do_exist = False
    for key, val in test_dict.items():
        if val == value:
            do_exist = True
    return do_exist

value = 43
# Iterate over all key, value pairs in dict and check if value exist
if check_value_exist(word_freq, value):
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")

# 3. Check if a value exists in a dictionary using any() and List comprehension

# Check if key exist in dictionary using any()
if any([True for k,v in word_freq.items() if v == value]):
    print(f"Yes, Value: '{value}' exists in dictionary")
else:
    print(f"No, Value: '{value}' does not exists in dictionary")

