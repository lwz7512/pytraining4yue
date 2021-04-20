# Mission:

# convert this series of BANK OF CHINA credit card number to xxxx-xxxx-xxxx-xxxx format
"""
4938093878851801
4938083578273646
4934729612151289
4938098913184167
4938083203974428
"""

# write a function to format the card numbers as:
"""
4938-0938-7885-1801
4938-0835-7827-3646
4934-7296-1215-1289
4938-0989-1318-4167
4938-0832-0397-4428
"""


# First step: seperate string to different group, one group 4 characters:

# 4938 --> group one,
# 0938 --> group two,
# 7885 --> group three,
# 1801 --> group four

card_number = '4938093878851801'

# we need 4 groups

groups = []

# this a stupid way:
groups.append(card_number[:4])
groups.append(card_number[4:8])
groups.append(card_number[8:12])
groups.append(card_number[12:])

print('>>> got the stupid groups: ')
print(groups)

# any smart way?
groups = []

group_start = ''
card_number_len = len(card_number)
for i in range(card_number_len):
  group_start += card_number[i]
  if len(group_start) == 4:
    groups.append(group_start)
    group_start = ''

print('>>>> got the smart groups: ')
print(groups)

# Second step: connect each group with '-'

result = '-'.join(groups)

print(result)

# write a function with a parameter ?

