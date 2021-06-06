# ====================================================
# Reading bbc learning english news

# in this example we will learn how to use:
# 1. BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/
# 2. pyttsx3
# https://pypi.org/project/pyttsx3/
# for pyttsx3 doc:
# https://pyttsx3.readthedocs.io/en/latest/engine.html

# and use these two library to get and read bbc news:
# https://www.bbc.co.uk/learningenglish/english/features/englishinthenews



# Before running code, install deps:
# pip3 install beautifulsoup4 requests pyttsx3



from bs4 import BeautifulSoup
import requests
import pyttsx3

# step 0: prepare speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    # to get the info. about various voices in our PC 
    print("---- Voice: ----")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages)

engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
# engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Victoria')
# engine.setProperty('voice', 'com.apple.speech.synthesis.voice.tingting')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# step 1: loading page
print('============================================')
print('>>>>  loading bbc learning english news...')
url = 'https://www.bbc.co.uk/learningenglish/english/features/englishinthenews'
response = requests.get(url)

# step 2: init beautifulsoup
soup = BeautifulSoup(response.content, 'html.parser')

# step 3: find the title of news
news = soup.select('.widget-bbcle-coursecontentlist-standard .course-content-item.active h2 > a')
# for n in news:
#     print('------------------')
#     print(n.get_text())

# step 4: read it
speak('Welcome to bbc learning english news!')
speak('today we have {0} news!'.format(len(news)))
counter = 0
for link in news:
    counter += 1
    print(link.get_text())
    print('-----------------')
    speak(str(counter))
    speak(link.get_text())

speak('These all are bbc features news, have a nice day!')