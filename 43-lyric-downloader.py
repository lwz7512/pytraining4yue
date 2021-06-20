# TODO: FROM https://www.azlyrics.com/
# USING: https://www.crummy.com/software/BeautifulSoup/
# DOC: https://tedboy.github.io/bs4_doc/index.html
# @2021/06/01

# before running this, install beautifulsoup:
# pip3 install beautifulsoup4

# in this example, you'll learn how to:
# 1. request webpage
# 2. parse webpage content
# 3. get the target section
# 4. write string to file

# for file operation:
# https://www.w3schools.com/python/python_file_write.asp

from typing import List
from bs4 import BeautifulSoup
import requests

# step 1: loading lyric web page for the song `anyone` from Justin Bieber
print('============================================')
print('>>>>  loading bbc learning lyric page ...')
url = 'https://www.azlyrics.com/lyrics/justinbieber/anyone.html'
response = requests.get(url)

# step 2: init beautifulsoup
soup = BeautifulSoup(response.content, 'html.parser')

# step 3: find the lyric block
lyric_block = soup.select('.col-xs-12.col-lg-8.text-center')
print(type(lyric_block)) # result set

# just need first one
result = lyric_block[0]
# find all the children in first level
divs_in_result = result.find_all('div', recursive=False) # recursive=False is important to get first level children
print(type(divs_in_result))

# counter = 0
# for div in divs_in_result:
#   print('===============:'+str(counter))
#   print(div)
#   counter += 1

# step 4: find the specific div
the_lyric = list(divs_in_result)[4]
print(type(the_lyric))

the_lyric_text = the_lyric.get_text()

print(the_lyric_text)

# step 5: write to file
f = open('data/anyone_lyric.txt', 'w')
with_title = 'Anyone - Justin Bieber\n' + the_lyric_text
f.write(with_title)