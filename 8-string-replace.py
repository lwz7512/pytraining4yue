# https://thispointer.com/python-replace-sub-strings-in-a-string-using-regex/
# https://thispointer.com/python-replace-character-in-string-by-index-position/
# https://thispointer.com/python-replace-multiple-characters-in-a-string/
# https://thispointer.com/python-string-replace-method/
# https://thispointer.com/python-replace-a-character-in-a-string/



### Python: Replace all whitespace characters from a string using regex

import re
org_string = "This is   a sample  string"
# Replace all whitespaces in a string with character X
new_string = re.sub(r"\s+", 'X', org_string)
print(new_string)

# Output: ThisXisXaXsampleXstring

# Syntax of the replace() function
# str.replace(old, new [, count])

### Python: Replace all occurrences of a substring in a string
sample_str = "This is a sample string, where is need to be replaced."
sample_str = sample_str.replace('is', 'ZZZ')
print(sample_str)
# output: ThZZZ ZZZ a sample string, where ZZZ need to be replaced.

### Python: Replace the first two occurrences of a substring in a string
org_string = "This is a sample string, where is need to be replaced."
sample_str = sample_str.replace('is', 'ZZZ', 2)
print(sample_str)

# output: ThZZZ ZZZ a sample string, where ZZZ need to be replaced.

