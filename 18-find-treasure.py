# Mission possible:
# iterate paths tree to find the red diamonds!

# TIP: using recursive loop
# @2021/04/27

flavors = ('sour', 'sweet', 'bitter', 'spicy', 'salty')
colors = ('golden', 'red', 'green', 'orange', 'purple')
treasures = ('diamond', 'gold', 'ruby', 'jade', 'aerolite', 'crystal')

amazing_fruit_tree = {
  'Apple': {
    'Ambrosia': {'flavor': 'sour', 'color': 'golden', 'treasure': 'diamond'},
    'Cortland': {'flavor': 'sweet', 'color': 'red', 'treasure': 'gold'},
    'Crispin':  {'flavor': 'bitter', 'color': 'green', 'treasure': 'ruby'},
    'Empire':   {'flavor': 'spicy', 'color': 'orange', 'treasure': 'jade'},
    'McIntosh': {'flavor': 'salty', 'color': 'purple', 'treasure': 'aerolite'},
    'Gala':     {'flavor': 'sour', 'color': 'golden', 'treasure': 'crystal'},
    'Fuji':     {'flavor': 'sweet', 'color': 'red', 'treasure': 'diamond'},
    'Idared':   {'flavor': 'bitter', 'color': 'green', 'treasure': 'gold',},
    'Honeycrisp': {'flavor': 'spicy', 'color': 'orange', 'treasure': 'ruby'},
    'Golden Delicious': {'flavor': 'salty', 'color': 'purple', 'treasure': 'jade'},
    },
  'Orange': {
    'Lukan':  {'flavor': 'sour', 'color': 'golden', 'treasure': 'aerolite'},
    'Ponkan': {'flavor': 'sweet', 'color': 'red', 'treasure': 'crystal'},
    'Swatow': {'flavor': 'bitter', 'color': 'green', 'treasure': 'diamond'},
    'Kinno':  {'flavor': 'spicy', 'color': 'orange', 'treasure': 'gold'},
    'Dekopon':{'flavor': 'salty', 'color': 'purple', 'treasure': 'ruby'},
  },
  'Banana': {
    'Apple Bananas':     {'flavor': 'sour', 'color': 'golden', 'treasure': 'jade'},
    'Cavendish Bananas': {'flavor': 'sweet', 'color': 'red', 'treasure': 'aerolite'},
    'LadysFinger Banana':{'flavor': 'bitter', 'color': 'green', 'treasure': 'crystal'},
    'Pisang Raja':       {'flavor': 'spicy', 'color': 'orange', 'treasure': 'diamond'},
    'Red Bananas':       {'flavor': 'salty', 'color': 'purple', 'treasure': 'gold'},
    'Cooking Bananas':   {'flavor': 'sour', 'color': 'golden', 'treasure': 'ruby'},
  },
  'Mongo': {
    'HONEY':   {'flavor': 'sweet', 'color': 'golden', 'treasure': 'jade'},
    'FRANCIS': {'flavor': 'bitter', 'color': 'red', 'treasure': 'aerolite'},
    'HADEN':   {'flavor': 'spicy', 'color': 'green', 'treasure': 'crystal'},
    'KEITT':   {'flavor': 'salty', 'color': 'orange', 'treasure': 'diamond'},
    'KENT':    {'flavor': 'sour', 'color': 'purple', 'treasure': 'gold'},
    'TOMMY ATKINS': {'flavor': 'sweet', 'color': 'golden', 'treasure': 'ruby'},
  },
  'Pear': {
    'GREEN ANJOU': {'flavor': 'bitter', 'color': 'red', 'treasure': 'jade'},
    'RED ANJOU':   {'flavor': 'spicy', 'color': 'green', 'treasure': 'aerolite'},
    'BARTLEFT':    {'flavor': 'salty', 'color': 'orange', 'treasure': 'crystal'},
    'RED BARTLEFT':{'flavor': 'sour', 'color': 'purple', 'treasure': 'diamond'},
    'BOSC':        {'flavor': 'sweet', 'color': 'golden', 'treasure': 'gold'},
    'COMICE':      {'flavor': 'bitter', 'color': 'red', 'treasure': 'ruby'},
    'CONCORDE':    {'flavor': 'salty', 'color': 'green', 'treasure': 'jade'},
    'FORELLE':     {'flavor': 'sour', 'color': 'orange', 'treasure': 'aerolite'},
    'SECKEL':      {'flavor': 'sweet', 'color': 'purple', 'treasure': 'crystal'},
    'STARKRIMSON': {'flavor': 'bitter', 'color': 'golden', 'treasure': 'diamond'},
  },
  'Lemon': {
    'Eureka Lemon': {'flavor': 'spicy', 'color': 'red', 'treasure': 'gold'},
    'Pink Variegated Lemon': {'flavor': 'salty', 'color': 'green', 'treasure': 'ruby'},
    'Lisbon Lemon ': {'flavor': 'sour', 'color': 'orange', 'treasure': 'jade'},
    'Meyer Lemon': {'flavor': 'sweet', 'color': 'purple', 'treasure': 'aerolite'},
    'Primofiori Lemon': {'flavor': 'bitter', 'color': 'golden', 'treasure': 'crystal'},
    'Verna Lemon': {'flavor': 'spicy', 'color': 'red', 'treasure': 'diamond'},
  },
  'Kiwi': {
    'Fuzzy kiwifruit': {'flavor': 'salty', 'color': 'green', 'treasure': 'gold'},
    'Kiwi berries':    {'flavor': 'sour', 'color': 'orange', 'treasure': 'ruby'},
    'Actinidia chinensis': {'flavor': 'sweet', 'color': 'purple', 'treasure': 'jade'},
  },
  'Plum': {
    'Briançon plum':{'flavor': 'bitter', 'color': 'golden', 'treasure': 'aerolite'},
    'cherry plum':  {'flavor': 'spicy', 'color': 'red', 'treasure': 'crystal'},
    'Italian plum': {'flavor': 'salty', 'color': 'green', 'treasure': 'diamond'},
    'damsons':      {'flavor': 'sour', 'color': 'orange', 'treasure': 'gold'},
    'Chinese plum': {'flavor': 'sweet', 'color': 'purple', 'treasure': 'ruby'},
    'blackthorn':   {'flavor': 'bitter', 'color': 'golden', 'treasure': 'jade'},
    'Alucha':       {'flavor': 'spicy', 'color': 'red', 'treasure': 'aerolite'},
  },
  'Peach': {
    'Yellow Peaches': {'flavor': 'salty', 'color': 'green', 'treasure': 'crystal'},
    'White Peaches':  {'flavor': 'sour', 'color': 'orange', 'treasure': 'diamond'},
    'Donut Peaches':  {'flavor': 'sweet', 'color': 'purple', 'treasure': 'ruby'},
    'Nectarines':     {'flavor': 'bitter', 'color': 'red', 'treasure': 'jade'},
  },
  'Apricot': {
    'Chinese Apricot': {'flavor': 'spicy', 'color': 'green', 'treasure': 'aerolite'},
    'Gold Cot':        {'flavor': 'salty', 'color': 'orange', 'treasure': 'crystal'},
    'Tilton':          {'flavor': 'sour', 'color': 'purple', 'treasure': 'diamond'},
    'Wenatchee':       {'flavor': 'sweet', 'color': 'red', 'treasure': 'gold'},
    'Goldbar':         {'flavor': 'bitter', 'color': 'green', 'treasure': 'ruby'},
    'Gold Kist':       {'flavor': 'spicy', 'color': 'orange', 'treasure': 'jade'},
    'Tomcot':          {'flavor': 'salty', 'color': 'purple', 'treasure': 'aerolite'},
    'Autumn Glo Apricot':    {'flavor': 'sour', 'color': 'golden', 'treasure': 'crystal'},
    'Brittany Gold Apricot': {'flavor': 'sweet', 'color': 'red', 'treasure': 'diamond'},
    'Canadian White Blenheim Apricot': {'flavor': 'bitter', 'color': 'green', 'treasure': 'gold'},
    'Harcot Apricot':  {'flavor': 'spicy', 'color': 'orange', 'treasure': 'ruby'},
    'Harglow Apricot': {'flavor': 'salty', 'color': 'purple', 'treasure': 'jade'},
  }
}


# --------- step 1: get key & value of the dict ------------
def traverseTree_1(node):
  for key in node:
    print('====>> THEKEY: ' + key)
    print('-----------------------')
    print(node[key])

# traverseTree_1(amazing_fruit_tree)

# --------- step 2: check the value type ----------------
def traverseTree_2(node):
  for key in node:
    print(type(node[key]) == dict)

# traverseTree_2(amazing_fruit_tree)

# --------- step 3: recursive loop the node
def traverseTree_3(node):
  if(type(node) == dict):
      print('===> this is a dict')
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
    traverseTree_7(sub_node, box)
  return box

total_red_diamond = traverseTree_7(amazing_fruit_tree, [])
print('the red diamonds in box: ' + str(len(total_red_diamond)))
