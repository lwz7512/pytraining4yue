# https://thispointer.com/python-how-to-sort-a-list-of-strings-list-sort-tutorial-examples/
# https://thispointer.com/python-sort-a-list-of-numbers-in-descending-or-ascending-order-list-sort-vs-sorted/

# Python : How to Sort a list of strings ? | list.sort() Tutorial & Examples

# By Alphabetical Order
# By Reverse Alphabetical Order
# By String Length
# By Numeric Order

# Suppose we have a list of strings i.e.

listOfStrings = ['hi' , 'hello', 'at', 'this', 'there', 'from']

# 1. Sort a List of strings in Alphabetical Order

'''
Sort List of string alphabetically
'''
sorted = listOfStrings.sort()
print(sorted)

# 2. Sort a List of strings alphabetically in Reverse Order
listOfStrings = ['hi' , 'hello', 'at', 'this', 'there', 'from']
sorted = listOfStrings.sort(reverse=True)
print(sorted)


# 3. Sort a List of string by Length

# usage: list.sort( key=function )

'''
Sort List of string by Length by using len() as custom key function 
'''
listOfStrings = ['hi' , 'hello', 'at', 'this', 'there', 'from']
sorted = listOfStrings.sort(key=len)
print(sorted)

# 4. Sort a List of string by Numeric Order

listOfNum = ['55' , '101', '152', '98', '233', '40', '67']

# To Sort a this list of strings by Numeric Order, provide int() as key function in sort i.e.
'''
Sort in Ascending numeric order, pass key function that should convert string to integer i.e using int()
'''
sorted = listOfNum.sort(key=int)
print(sorted)


# 5. Sorting a list of strings by Numerically in descending Order

'''
Sort in Descending numeric order, pass reverse flag along with key function
'''
listOfNum = ['55' , '101', '152', '98', '233', '40', '67']
sorted = listOfNum.sort(reverse=True, key=int)
print(sorted)




####   Python : Sort a List of numbers in Descending or Ascending Order | list.sort() vs sorted()


# Suppose we have a list of number’s i.e.

# List of numbers
listOfNum = [23, 45, 21, 45, 2, 5, 11, 50, 1, 67]

# 1. Sorting the List in ascending Order using sorted()

# Create a sorted copy of existing list
newList = sorted(listOfNum)

print(newList)
print(listOfNum) # not changed

# 2. Sorting the List in ascending Order using list.sort()
# Sort the List in Place
listOfNum = [23, 45, 21, 45, 2, 5, 11, 50, 1, 67]
listOfNum.sort()
print(listOfNum) # changed


# 3. Sorting the List in Descending Order using sorted()

# Create a sorted (Descending Order) copy of existing list
listOfNum = [23, 45, 21, 45, 2, 5, 11, 50, 1, 67]
newList = sorted(listOfNum, reverse=True)
print(newList)
print(listOfNum)

# 4. Sorting the List in Descending Order using list.sort()

# Sort the List in Place (Descending Order)
listOfNum = [23, 45, 21, 45, 2, 5, 11, 50, 1, 67]
listOfNum.sort(reverse=True)
print(listOfNum) # changed

# output: [67, 50, 45, 45, 23, 21, 11, 5, 2, 1]


