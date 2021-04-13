"""
== Missions: 
1. How to Remove Duplicates From a Python List;
2. Check one element in a list if contains duplicates;
3. Count the duplicate words in one sentence;
4. Create a function to find the first repeated word in a sentence;

== Knowledge points we would learn:
1. dict
2. string split
3. set

== Reference:
Python List count() Method
https://www.w3schools.com/python/ref_list_count.asp

Python List/Array Methods
https://www.w3schools.com/python/python_ref_list.asp

Python Dictionaries
https://www.w3schools.com/python/python_dictionaries.asp

Python Sets
https://www.w3schools.com/python/python_sets.asp

"""

### ask yourself: 
# what's the difference between dict and set?

# thisIsdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# thisIsset = {"apple", "banana", "cherry"}


### mission 1: How to Remove Duplicates From a Python List;
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# or use set function remove duplicates
your_list = ['one', 'two', 'one']
no_dup_list = set(your_list)
print(no_dup_list)

# ### mission 2: Check one element in a list if contains duplicates;
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
okCount = listOfElems.count('Ok')
print(">>> Ok occurrens times: ", okCount)

### mission 3: Count the duplicate words in one sentence;
mysentence = "As far as the laws of mathematics refer to reality they are not certain as far as they are certain they do not refer to reality"

words = mysentence.split()
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
print(counts)

### mission 4: Create a function to find the first repeated word in a sentence;

"""
Algorithm:

repeatedWord(str)
Step 1: first split given string separated by space into words.
Step 2: now convert the list of words into a dictionary.
Step 3: traverse list of words and check which the first word has frequency >1
"""
def firstRepeatedWord(str):
  words = str.split(' ')
  counts = {}
  for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
  
  for word in words:
    if counts[word] > 0:
      return word

word = firstRepeatedWord(mysentence)

print(word)