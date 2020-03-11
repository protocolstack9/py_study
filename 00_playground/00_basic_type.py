from pydebug import GetFrame

type_of_python = ''' type of python

    Python is strongly typed, which means that the type of an object does not change,
    even if its value is mutable
'''
a = True
b = 3.141592
x = 5
s = "geeksforgeeks"
y = [1,2,3] 
print(type(a))  # bool
print(type(b))  # float
print(type(x))  # int
print(type(s))  # str
print(type(y))  # list
print(type({})) # dict
print(type([])) # list
print(type(())) # tuple
print(type(type(a))) # type

div_mod = divmod(9,5)
print(div_mod, type(div_mod)) # (1, 4) tuple

''' reserved keywords:

False class finally is return
None continue for lambda try
True def from nonlocal while
and del global not with
as elif if or yield
assert else import pass
break except in raise
'''


''' bases
  0b or 0B for binary (base 2)
  0o or 0O for octal (base 8)
  0x or 0X for hex (base 16)
'''


# ############################################################
# string  
# ############################################################
print(int(1.0e4)) # 10000
print(str(1.0e4)) # 10000.0
hello = "Hello"
world = "World!"
print(hello, world) # with space
print(hello + world) # without space

start = 'Na ' * 4 + '\n' # Na Na Na Na
middle = 'Hey ' * 3 + '\n' # Hey Hey Hey
end = 'Goodbye.'
print(start + start + middle + end)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-1]) # 'z'
print(letters[:-1]) # 'abcdefghijklmnopqrstuvwxyz'
print(letters[::2]) # 'acegikmoqsuwy'

name = 'Henny'
print(name.replace('H', 'P'))  # XXX name[0] = 'H'
print('P' + name[1:])

print(len(name)) # 5

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
print(todos.split(',')) # ['get gloves', 'get mask', 'give cat vitamins', 'call ambulance']
print(todos.split()) # ['get', 'gloves,get', 'mask,give', 'cat', 'vitamins,call', 'ambulance']

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string) # Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster

# poem.startswith('All') # return boolean
# poem.endswith('That\'s all, folks!')
# poem.find(word)
# poem.rfind(word)
# poem.count(word)
# poem.isalnum()         # return boolean

# setup.strip('.')
# setup.capitalize()
# setup.title()     # capitalize all the words
# setup.upper()
# setup.lower() 
# setup.swapcase()  # swap upper- and lowercase

# setup.center(30)  # Center the string within 30 spaces
# setup.ljust(30)   # Left justify
# setup.rjust(30)   # Right justify

re = type_of_python.replace('strongly', 'weakly') # copy
print(type_of_python)
print(re)

# ############################################################
# lists
# ############################################################
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))         # ['ready', 'fire', 'aim']
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[1], marxes[-1]) # 'Chico', 'Harpo'
print(marxes[::-1])          # reverse ['Harpo', 'Chico', 'Groucho']

# Add an Item to the End with append()
marxes.append('Zeppo')       # Add an Item to the End

# Combine Lists by Using extend() or +=
others = ['Gummo', 'Karl']
others2 = ['others']
marxes.extend(others)        # .append(others) -> ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]
print(marxes)                # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']
marxes += others2
print(marxes)                # ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl', 'others']

# Add an Item by Offset with insert()
marxes.insert(3, 'totti')
print(marxes)                # ['Groucho', 'Chico', 'Harpo', 'totti', 'Zeppo', 'Gummo', 'Karl', 'others']

# Delete an Item by Offset with del
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
print(marxes[2]) # 'Harpo'
del marxes[2]
print(marxes[2]) # 'Harpo'
print(marxes)    # ['Groucho', 'Chico', 'Gummo', 'Zeppo']

# Delete an Item by Value with remove()
marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
print(marxes)    # ['Groucho', 'Chico', 'Harpo', 'Zeppo']

# Get an Item by Offset and Delete It by Using pop()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()     # default -1. 'Zeppo'
print(marxes)    # ['Groucho', 'Chico', 'Harpo']
marxes.pop(1)    # 'Chico'
print(marxes)    # ['Groucho', 'Harpo']

# Find an Item’s Offset by Value with index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Harpo']
print(marxes.index('Harpo'))     # 2
print(marxes.index('Harpo', 3))  # 4

# Test for a Value with in
print('Groucho' in marxes)       # True
print('Bob' in marxes)           # False

# Count Occurrences of a Value by Using count()
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))  # 3

# Convert to a String with join()
friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)  #'Harry * Hermione * Ron'
separated = joined.split(separator)
print(separated) # ['Harry', 'Hermione', 'Ron']
print(separated == friends) # True

# Reorder Items with sort()
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes) # The general function sorted() returns a sorted copy of the list.
print(sorted_marxes) # '['Chico', 'Groucho', 'Harpo']

marxes.sort() # The list function sort() sorts the list itself, in place.
print(marxes) # ['Chico', 'Groucho', 'Harpo']

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers) # [4.0, 3, 2, 1]

# Get Length by Using len()
marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes)) # 3

# Assign with =, Copy with copy()
a = [1, 2, 3]
b = a       # b just refers to the same list object as a
a[0] = 10
print(b[0]) # 10
''' copy
  The list copy() function       => b = a.copy()
  The list() conversion function => c = list(a)
  The list slice [:]             => d = a[:]
'''

print("[file] %s, [func] %s, [line] %s" % (GetFrame("file"), GetFrame("func"), GetFrame("line")))



# ############################################################
# tuples
# ############################################################

# empty tuple
empty_tuple = ()
print(type(empty_tuple))

# tuple unpacking
marx_tuple = 'Groucho', 'Chico', 'Harpo' # it’s the trailing commas that really define a tuple
a, b, c = marx_tuple
print(a, b, c) # Groucho Chico Harpo

# exchange values without temporary variable
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password, icecream) # tuttifrutti swordfish

marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)
print(marx_list) # ('Groucho', 'Chico', 'Harpo')

""" why use tuples?
• Tuples use less space.
• You can’t clobber tuple items by mistake.
• You can use tuples as dictionary keys (see the next section).
• Named tuples (see “Named Tuples” on page 141) can be a simple alternative to objects.
• Function arguments are passed as tuples (see “Functions” on page 85).
"""



# ############################################################
# dict 
# ############################################################

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(dict(lol)) # {'a': 'b', 'c': 'd', 'e': 'f'}

#any sequence containing two-item sequences
los = [ 'ab', 'cd', 'ef' ]
print(dict(los)) # {'a': 'b', 'c': 'd', 'e': 'f'}

# add to dict
pythons = {
  'Chapman': 'Graham',
  'Cleese': 'John',
  'Doe': 'Jane',
}
pythons['Gilliam'] = 'Terry'

# Combine Dictionaries with update()
python_others = {
  'Doe': 'John' # update with value of the key 'Doe'
}
pythons.update(python_others)
print(pythons) # {'Chapman': 'Graham', 'Cleese': 'John', 'Doe': 'John', 'Gilliam': 'Terry'}

# Delete an Item by Key with del
del(pythons['Cleese']) # {'Chapman': 'Graham', 'Doe': 'John', 'Gilliam': 'Terry'}
print(pythons) 

# Delete All Items by Using clear()
pythons2 = dict(pythons)
pythons2.clear()
print(pythons2) 

# Test for a Key by Using in
print('Doe' in pythons)    # True
print('Cleese' in pythons) # False

# Get an Item by [ key ]
print(pythons.get('Chapman')) # Graham
print(pythons.get('Cleese', 'deleted')) # deleted

# Get All Keys by Using keys()
print(pythons.keys())   # dict_keys(['Chapman', 'Doe', 'Gilliam'])
# Get All Values by Using values()
print(list(pythons.values())) # ['Graham', 'John', 'Terry']

# Get All Key-Value Pairs by Using items()
print(pythons.items()) # tuple - ('Chapman', 'Graham'), ('Doe', 'John'), ('Gilliam', 'Terry')

# Assign with =, Copy with copy()
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)          # {'blue': 'confuse everyone', 'green': 'go', 'red': 'smile for the camera', 'yellow': 'go faster'}
print(original_signals) # {'green': 'go', 'red': 'smile for the camera', 'yellow': 'go faster'}



# ############################################################
# set
# ############################################################
# A set is like a dictionary with its values thrown away, leaving only the keys.
# You can create a set from a list, string, tuple, or dictionary, discarding any duplicate values.

empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}

print(set("letter")) # {'t', 'l', 'e', 'r'}

# Test for Value by Using in
drinks = {
  'martini': {'vodka', 'vermouth'},
  'black russian': {'vodka', 'kahlua'},
  'white russian': {'cream', 'kahlua', 'vodka'},
  'manhattan': {'rye', 'vermouth', 'bitters'},
  'screwdriver': {'orange juice', 'vodka'}
}
for name, contents in drinks.items():
  if 'vodka' in contents:
    print(name)
# martini
# black russian
# white russian
# screwdriver
for name, contents in drinks.items():
  if contents & {'vermouth', 'orange juice'}:
    print(name)
# martini
# manhattan
# screwdriver

# intersection) & or the set intersection() function
# union) | or the set union() function
# difference) - or difference() function
# exclusive) ^ or symmetric_difference() function
# subset) <= or issubset()
# proper subset) <
# superset) >= or issuperset()
# proper superset) >

# tuple is immutable so it can be dict key
houses = {
  (44.79, -93.14, 285): 'My House',
  (38.89, -77.03, 13): 'The White House'
 }