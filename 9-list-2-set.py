# https://thispointer.com/7-ways-to-add-all-elements-of-list-to-set-in-python/

### 7 Ways to add all elements of list to set in python
# 
# Suppose we have a list and a set i.e.

sample_set = {11, 12, 13, 14}
list_of_num = [10, 11, 12, 13, 14, 15, 16]

# Now we want to add all the elements of the list to the set. As set contains only unique elements, so after adding elements from a list to the set, the contents of set should be like,
# {10, 11, 12, 13, 14, 15, 16}

# 1. Add all elements of a list to set using update() function
# set.update(sequences)

# Create and intialize a set
sample_set = {11, 12, 13, 14}
# a list of numbers
list_of_num = [10, 11, 12, 13, 14, 15, 16]
# add all elements in list to the set
sample_set.update(list_of_num)
print('Modified Set: ')
print(sample_set)

# 2. Adding a list to set using add() function
# set.add(element)

# A set of numbers
sample_set = {11, 12, 13, 14}
# a list of numbers
list_of_num = [10, 11, 12, 13, 14, 15, 16]
# Iterate over all elements of list and
for elem in list_of_num:
    # add each element to the set
    sample_set.add(elem)
print('Modified Set: ')
print(sample_set)

# 3. Add a list to set using add() & union()
# s.union(t)
sample_set = {11, 12, 13, 14}
list_of_num = [10, 11, 12, 13, 14, 15, 16]
# convert list to set and get union of both the sets
sample_set = sample_set.union(set(list_of_num))
print('Modified Set: ')
print(sample_set)

# 4. Add all elements in a list to set using | operator
sample_set = {11, 12, 13, 14}
list_of_num = [10, 11, 12, 13, 14, 15, 16]
# convert list to set and get union of both the sets using |
sample_set |= set(list_of_num)
print('Modified Set: ')
print(sample_set)

# 5. Add a list to set using |= and unpacking list to set
sample_set = {11, 12, 13, 14}
list_of_num = [10, 11, 12, 13, 14, 15, 16]
# unpack list to a set and OR that with original set
sample_set |= {*list_of_num}
print('Modified Set: ')
print(sample_set)

# 6. Adding all elements from multiple lists to the set
# 3 lists of numbers
list_num_1 = [15, 16, 17]
list_num_2 = [18, 19]
list_num_3 = [30, 31, 19, 17]

# A set of numbers
sample_set = {11, 12, 13, 14}
# Add multiple lists
sample_set.update(list_num_1, list_num_2, list_num_3)
print('Modified Set: ')
print(sample_set)
