# https://stackoverflow.com/questions/2612802/list-changes-unexpectedly-after-assignment-why-is-this-and-how-to-prevent-it

# 1. lis copy()

old_list = [1, 2, 3, 4]

new_list = old_list.copy()

# 2. use slice

new_list = old_list[:]

# 3. list function

new_list = list(old_list)



