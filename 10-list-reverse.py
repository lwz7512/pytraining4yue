# https://thispointer.com/python-reverse-a-list-sub-list-or-list-of-list-in-place-or-copy/

# Python: Reverse a list, sub list or list of list | In place or Copy

# Suppose we have a list,
list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]

# 1. Get a reversed list using reversed() function
# reversed(seq)

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Get a list with reversed contents
reversed_list = list(reversed(list_of_num))
print(reversed_list)

# 2. Get a reversed list using slicing
# list[start:stop:step_size]

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Get a reversed list by providing step size as -1
reversed_list = list_of_num[::-1]
print('Reversed list: ')
print(reversed_list)

# 3. Get a reversed list using for loop

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Create an empty list
reversed_list = []
# loop from 0 to len -1 i.e. size of list
for i in range(len(list_of_num)):
    # Append element at index -i to the new list
    reversed_list.append(list_of_num[-(i+1)])
print('Reversed list: ')
print(reversed_list)


# 4. Get a reversed list using list comprehension

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Iterate over num 0 to size-1 and select elements from back i.e. -i
reversed_list = [list_of_num[-(i+1)] for i in range(len(list_of_num))]
print(reversed_list)

# 5. Reverse the contents of a list in place

list_of_num = [51, 52, 53, 54, 55, 56, 57, 58, 59]
# Reverse the contents of a list in place
list_of_num.reverse()
print(reversed_list)

