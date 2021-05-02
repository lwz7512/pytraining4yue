# Mission possible:
# iterate paths tree to find the red diamonds!

# TIP: using recursive loop
# @2021/04/27

# for wiki reference:
# https://en.wikipedia.org/wiki/Recursion_(computer_science)


# ------- Factorial - 阶乘 for example:  -----------
# 7 * 6 * 5 * 4 * 3 * 2 * 1
# Factorial of a number using recursion
def recur_factorial(n):
  print(n)
  if n == 1:
    return n
  else:
    return n*recur_factorial(n-1)

num = 3

# check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))


# --- Python program to display the Fibonacci sequence ----
# Fibonacci sequence:
# 0 1 1 2 3 5 8 13 21 34

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))


# -------------  treasure tree structure ------------------
# to find all the red diamonds.
flavors = ('sour', 'sweet', 'bitter', 'spicy', 'salty')
colors = ('golden', 'red', 'green', 'orange', 'purple')
treasures = ('diamond', 'gold', 'ruby', 'jade', 'aerolite', 'crystal')

amazing_fruit_tree = {
  'id': 0,
  'Apple': {
    'id': 1,
    'Ambrosia': {'id': 11, 'flavor': 'sour', 'color': 'golden', 'treasure': 'diamond'},
    'Cortland': {'id': 12, 'flavor': 'sweet', 'color': 'red', 'treasure': 'gold'},
    'Crispin':  {'id': 13, 'flavor': 'bitter', 'color': 'green', 'treasure': 'ruby'},
    'Empire':   {'id': 14, 'flavor': 'spicy', 'color': 'orange', 'treasure': 'jade'},
    'McIntosh': {'id': 15, 'flavor': 'salty', 'color': 'purple', 'treasure': 'aerolite'},
    'Gala':     {'id': 16, 'flavor': 'sour', 'color': 'golden', 'treasure': 'crystal'},
    'Fuji':     {'id': 17, 'flavor': 'sweet', 'color': 'red', 'treasure': 'diamond'},
    'Idared':   {'id': 18, 'flavor': 'bitter', 'color': 'green', 'treasure': 'gold',},
    'Honeycrisp': {'id': 19, 'flavor': 'spicy', 'color': 'orange', 'treasure': 'ruby'},
    'Golden Delicious': {'id': 20, 'flavor': 'salty', 'color': 'purple', 'treasure': 'jade'},
    },
  'Orange': {
    'id': 2,
    'Lukan':  {'id': 21, 'flavor': 'sour', 'color': 'golden', 'treasure': 'aerolite'},
    'Ponkan': {'id': 22, 'flavor': 'sweet', 'color': 'red', 'treasure': 'crystal'},
    'Swatow': {'id': 23, 'flavor': 'bitter', 'color': 'green', 'treasure': 'diamond'},
    'Kinno':  {'id': 24, 'flavor': 'spicy', 'color': 'orange', 'treasure': 'gold'},
    'Dekopon':{'id': 25, 'flavor': 'salty', 'color': 'purple', 'treasure': 'ruby'},
  },
  'Banana': {
    'id': 3,
    'Apple Bananas':     {'id': 26, 'flavor': 'sour', 'color': 'golden', 'treasure': 'jade'},
    'Cavendish Bananas': {'id': 27, 'flavor': 'sweet', 'color': 'red', 'treasure': 'aerolite'},
    'LadysFinger Banana':{'id': 28, 'flavor': 'bitter', 'color': 'green', 'treasure': 'crystal'},
    'Pisang Raja':       {'id': 29, 'flavor': 'spicy', 'color': 'orange', 'treasure': 'diamond'},
    'Red Bananas':       {'id': 30, 'flavor': 'salty', 'color': 'purple', 'treasure': 'gold'},
    'Cooking Bananas':   {'id': 31, 'flavor': 'sour', 'color': 'golden', 'treasure': 'ruby'},
  },
  'Mongo': {
    'id': 4,
    'HONEY':   {'id': 31, 'flavor': 'sweet', 'color': 'golden', 'treasure': 'jade'},
    'FRANCIS': {'id': 32, 'flavor': 'bitter', 'color': 'red', 'treasure': 'aerolite'},
    'HADEN':   {'id': 33, 'flavor': 'spicy', 'color': 'green', 'treasure': 'crystal'},
    'KEITT':   {'id': 34, 'flavor': 'salty', 'color': 'orange', 'treasure': 'diamond'},
    'KENT':    {'id': 35, 'flavor': 'sour', 'color': 'purple', 'treasure': 'gold'},
    'TOMMY ATKINS': {'id': 36, 'flavor': 'sweet', 'color': 'golden', 'treasure': 'ruby'},
  },
  'Pear': {
    'id': 5,
    'GREEN ANJOU': {'id': 37, 'flavor': 'bitter', 'color': 'red', 'treasure': 'jade'},
    'RED ANJOU':   {'id': 38, 'flavor': 'spicy', 'color': 'green', 'treasure': 'aerolite'},
    'BARTLEFT':    {'id': 39, 'flavor': 'salty', 'color': 'orange', 'treasure': 'crystal'},
    'RED BARTLEFT':{'id': 40, 'flavor': 'sour', 'color': 'purple', 'treasure': 'diamond'},
    'BOSC':        {'id': 41, 'flavor': 'sweet', 'color': 'golden', 'treasure': 'gold'},
    'COMICE':      {'id': 42, 'flavor': 'bitter', 'color': 'red', 'treasure': 'ruby'},
    'CONCORDE':    {'id': 43, 'flavor': 'salty', 'color': 'green', 'treasure': 'jade'},
    'FORELLE':     {'id': 44, 'flavor': 'sour', 'color': 'orange', 'treasure': 'aerolite'},
    'SECKEL':      {'id': 45, 'flavor': 'sweet', 'color': 'purple', 'treasure': 'crystal'},
    'STARKRIMSON': {'id': 46, 'flavor': 'bitter', 'color': 'golden', 'treasure': 'diamond'},
  },
  'Lemon': {
    'id': 6,
    'Eureka Lemon': {'id': 47, 'flavor': 'spicy', 'color': 'red', 'treasure': 'gold'},
    'Pink Variegated Lemon': {'id': 48, 'flavor': 'salty', 'color': 'green', 'treasure': 'ruby'},
    'Lisbon Lemon ': {'id': 49, 'flavor': 'sour', 'color': 'orange', 'treasure': 'jade'},
    'Meyer Lemon': {'id': 50, 'flavor': 'sweet', 'color': 'purple', 'treasure': 'aerolite'},
    'Primofiori Lemon': {'id': 51, 'flavor': 'bitter', 'color': 'golden', 'treasure': 'crystal'},
    'Verna Lemon': {'id': 52, 'flavor': 'spicy', 'color': 'red', 'treasure': 'diamond'},
  },
  'Kiwi': {
    'id': 7,
    'Fuzzy kiwifruit': {'id': 53, 'flavor': 'salty', 'color': 'green', 'treasure': 'gold'},
    'Kiwi berries':    {'id': 54, 'flavor': 'sour', 'color': 'orange', 'treasure': 'ruby'},
    'Actinidia chinensis': {'id': 55, 'flavor': 'sweet', 'color': 'purple', 'treasure': 'jade'},
  },
  'Plum': {
    'id': 8,
    'Briançon plum':{'id': 56, 'flavor': 'bitter', 'color': 'golden', 'treasure': 'aerolite'},
    'cherry plum':  {'id': 57, 'flavor': 'spicy', 'color': 'red', 'treasure': 'crystal'},
    'Italian plum': {'id': 58, 'flavor': 'salty', 'color': 'green', 'treasure': 'diamond'},
    'damsons':      {'id': 59, 'flavor': 'sour', 'color': 'orange', 'treasure': 'gold'},
    'Chinese plum': {'id': 60, 'flavor': 'sweet', 'color': 'purple', 'treasure': 'ruby'},
    'blackthorn':   {'id': 61, 'flavor': 'bitter', 'color': 'golden', 'treasure': 'jade'},
    'Alucha':       {'id': 62, 'flavor': 'spicy', 'color': 'red', 'treasure': 'aerolite'},
  },
  'Peach': {
    'id': 9,
    'Yellow Peaches': {'id': 63, 'flavor': 'salty', 'color': 'green', 'treasure': 'crystal'},
    'White Peaches':  {'id': 64, 'flavor': 'sour', 'color': 'orange', 'treasure': 'diamond'},
    'Donut Peaches':  {'id': 65, 'flavor': 'sweet', 'color': 'purple', 'treasure': 'ruby'},
    'Nectarines':     {'id': 66, 'flavor': 'bitter', 'color': 'red', 'treasure': 'jade'},
  },
  'Apricot': {
    'id': 10,
    'Chinese Apricot': {'id': 67, 'flavor': 'spicy', 'color': 'green', 'treasure': 'aerolite'},
    'Gold Cot':        {'id': 68, 'flavor': 'salty', 'color': 'orange', 'treasure': 'crystal'},
    'Tilton':          {'id': 69, 'flavor': 'sour', 'color': 'purple', 'treasure': 'diamond'},
    'Wenatchee':       {'id': 70, 'flavor': 'sweet', 'color': 'red', 'treasure': 'gold'},
    'Goldbar':         {'id': 71, 'flavor': 'bitter', 'color': 'green', 'treasure': 'ruby'},
    'Gold Kist':       {'id': 72, 'flavor': 'spicy', 'color': 'orange', 'treasure': 'jade'},
    'Tomcot':          {'id': 73, 'flavor': 'salty', 'color': 'purple', 'treasure': 'aerolite'},
    'Autumn Glo Apricot':    {'id': 74, 'flavor': 'sour', 'color': 'golden', 'treasure': 'crystal'},
    'Brittany Gold Apricot': {'id': 75, 'flavor': 'sweet', 'color': 'red', 'treasure': 'diamond'},
    'Canadian White Blenheim Apricot': {'id': 76, 'flavor': 'bitter', 'color': 'green', 'treasure': 'gold'},
    'Harcot Apricot':  {'id': 77, 'flavor': 'spicy', 'color': 'orange', 'treasure': 'ruby'},
    'Harglow Apricot': {'id': 78, 'flavor': 'salty', 'color': 'purple', 'treasure': 'jade'},
  }
}


# --------- step 1: get key & value of the dict ------------
def traverseTree_1(node):
  for key in node:
    print('====>> THEKEY: ' + key)
    print('-----------------------')
    # print(node[key])

# traverseTree_1(amazing_fruit_tree)

# --------- step 2: check the value type ----------------
def traverseTree_2(node):
  for key in node:
    print(type(node[key]) == dict)

# traverseTree_2(amazing_fruit_tree)

# --------- step 3: recursive loop the nodet
def traverseTree_3(node):
  if(type(node) == dict):
      print('===> this is a dict, id: {0}'.format(node.get('id')))
  for key in node:
    sub_node = node[key]
    if(type(sub_node) == dict):
      traverseTree_3(sub_node)  # recursive loop !!!

# traverseTree_3(amazing_fruit_tree)

# ---------- step 4: check the color, and the treasure type
def traverseTree_4(node):
  if(type(node) == dict):
      print('===> this is a dict')
      print(node.get('color'))
      print(node.get('treasure'))
      print('----------------------')
  for key in node:
      sub_node = node[key]
      if(type(sub_node) == dict):
        traverseTree_4(sub_node)  # recursive loop !!!
    
# traverseTree_4(amazing_fruit_tree)

# ----------- step 5: check color value, and treasure value ------
def traverseTree_5(node):
  if(type(node) == dict):
      if(node.get('color') == 'red' and node.get('treasure') == 'diamond'):
        print('>>>>>>>>> got one!')
  for key in node:
      sub_node = node[key]
      if(type(sub_node) == dict):
        traverseTree_5(sub_node)  # recursive loop !!!

# traverseTree_5(amazing_fruit_tree)

# -----------  step 6: count the red diamond -----------------
red_diamond_num = 0
def traverseTree_6(node):
  if(type(node) == dict):
      if(node.get('color') == 'red' and node.get('treasure') == 'diamond'):
        print('>>>>>>>>> got one!')
        global red_diamond_num
        red_diamond_num += 1
  for key in node:
      sub_node = node[key]
      if(type(sub_node) == dict):
        traverseTree_6(sub_node)  # recursive loop !!!

# traverseTree_6(amazing_fruit_tree)
# print('got the red diamond number: ' + str(red_diamond_num))

# ------------ step 7: put the counter inside the loop ------
def traverseTree_7(node, box):
  if(type(node) == dict):
      if(node.get('color') == 'red' and node.get('treasure') == 'diamond'):
        print('>>>>>>>>> got one!')
        box.append(0)
  for key in node:
    if(type(node) != dict):
      continue
    sub_node = node[key]
    if (type(sub_node) == dict):
      traverseTree_7(sub_node, box)
  return box

# total_red_diamond = traverseTree_7(amazing_fruit_tree, [])
# print('the red diamonds in box: ' + str(len(total_red_diamond)))
