"""
== Missions: 
1. Create a list(size/length 100) by dynamically putting 100 numbers into it from 1 to 100;
2. Calculate the sum of numbers sequence 1~100;


== Knowledge points we would learn:
1. list and list initialization usage
2. loop command
3. print function
4. len function
5. list function

== Reference:
Range function
https://www.w3schools.com/python/ref_func_range.asp

Python Built in Functions
https://www.w3schools.com/python/python_ref_functions.asp

More tiny conceptual examples
https://www.w3schools.com/python/python_examples.asp

Chinese examples
https://www.runoob.com/python/python-100-examples.html
"""

nums_list = []  # this is a blank list
nums_size = 100 # define this size
nums_range = range(1, nums_size+1) # create a range, with range function

# print(type(nums_range))
# print(type(nums_list))

# -- APPROACH 1 to fill the nums_list:
# use for loop to fill the list from range
# https://www.w3schools.com/python/python_while_loops.asp
# for x in nums_range:
#   nums_list.append(x)

# -- APPROACH 2  to fill the nums_list:
# this way more simpler:
# nums_list.extend(nums_range)

# -- APPROACH 3 to fill the nums_list
# use list function to initialize:
# https://www.w3schools.com/python/ref_func_list.asp
nums_list = list(nums_range)

print("the nums list size is: ", len(nums_list)) # use len() to check size of list
print(">>> haha! mission 1 completed! <<<")
print("lets check the first element of the list: ", nums_list[0])
print("lets check the second element of the list: ", nums_list[1])
print("lets check the last element of the list: ", nums_list[-1])

# so, ask youself: 
# how to fill a list with the same value for example 0?
# here's the answer:
# https://thispointer.com/python-how-to-create-a-list-and-initialize-with-same-values/
# same_element_list = [0] * 100
# print(same_element_list)

# now, we calculate the sum of 100 nums:
sum_of_100_nums = 0 # define a initial value
# use for loop again to add
for x in nums_list:
  sum_of_100_nums += x  # this equal to: sum_of_100_nums = sum_of_100_nums + x
  # sum_of_100_nums = sum_of_100_nums + x
# we got the sum now:
print(">>> mission 2 accomplished, the sum of 100 numbers is: ", sum_of_100_nums)


# at last, we could need to know how to use one line to complete mission 2:
# https://www.w3schools.com/python/ref_func_sum.asp
sum_of_100_nums = sum(range(1, nums_size+1))
print(">>> mission in one line, the sum of 100 numbers is: ", sum_of_100_nums)

