# import the random module
import random


def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

def print_hand(hand, name='Guest'):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

def judge(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'Lose'
    elif player == 1 and computer == 2:
        return 'Lose'
    elif player == 2 and computer == 0:
        return 'Lose'
    else:
        return 'Win'


FLAG = 0

print('Starting the Rock Paper Scissors game!')
player_name = input('Please enter your name: ') # Takes Input from the user

while FLAG < 3:
  print('Pick a hand: (0: Rock, 1: Paper, 2: Scissors), or press 3 to exit!')
  player_hand = int(input('Please enter a number (0-2): '))

  FLAG = player_hand

  if validate(player_hand):
      # Assign a random number between 0 and 2 to computer_hand using randint
      computer_hand = random.randint(0, 2)
      
      print_hand(player_hand, player_name)
      print_hand(computer_hand, 'Computer')

      result = judge(player_hand, computer_hand)
      print('Result: ' + result)
  else:
      print('Exit!')

