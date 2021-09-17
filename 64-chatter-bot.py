# Create an AI Chat Bot
# @2021/08/24
# https://www.datacamp.com/community/tutorials/building-a-chatbot-using-chatterbot
# https://chatterbot.readthedocs.io/en/stable/
# https://github.com/gunthercox/ChatterBot
# 
# -----------------------------------
# pyenv install first
# -----------------------------------
# https://github.com/pyenv/pyenv
# https://amaral.northwestern.edu/resources/guides/pyenv-tutorial
# % brew update
# % brew install pyenv
# % echo 'eval "$(pyenv init --path)"' >> ~/.zprofile
# % source .zprofile
# 
# install & use python 3.6.6 :
# % pyenv install 3.6.0
# % pyenv global 3.6.0
# 
# -----------------------------------
# Install spaCy with python 3.6.0 :
# -----------------------------------
# % python -m pip install -U pip setuptools                # install/update build tools
# % pip install wheel==0.32.0 cython numpy==1.15.0         # install wheel with new pip
# % MACOSX_DEPLOYMENT_TARGET="11.4" pip install blis==0.2.4
# % pip install spacy==2.1.0                               # install spacy 2.1.0
# % python -m spacy download en                            # download default model

# ----------------------------------
# Install chatterbot 0.7.6 with python 3.6.0
# 
# https://github.com/gunthercox/ChatterBot/tree/0.7.6/examples

# pip install chatterbot==0.7.6

from chatterbot import ChatBot

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# ai.yml Training: [####################] 100%
# botprofile.yml Training: [####################] 100%
# computers.yml Training: [####################] 100%
# conversations.yml Training: [####################] 100%
# drugs.yml Training: [####################] 100%
# emotion.yml Training: [####################] 100%
# alias ..='cd ..'
# food.yml Training: [####################] 100%
# gossip.yml Training: [####################] 100%
# greetings.yml Training: [####################] 100%
# history.yml Training: [####################] 100%
# humor.yml Training: [####################] 100%
# literature.yml Training: [####################] 100%
# money.yml Training: [####################] 100%
# movies.yml Training: [####################] 100%
# politics.yml Training: [####################] 100%
# psychology.yml Training: [####################] 100%
# science.yml Training: [####################] 100%
# sports.yml Training: [####################] 100%
# trivia.yml Training: [####################] 100%

# Get a response to an input statement
# https://chatterbot-corpus.readthedocs.io/en/latest/data.html
greeting = 'Hello, how are you today?'
print('>>> ' + greeting)
response = chatbot.get_response(greeting)
print(response)

greeting = 'Good day to you sir!'
print('>>> ' + greeting)
response = chatbot.get_response(greeting)
print(response)
