### print("[file] %s, [func] %s, [line] %s" % (GetFrame("file"), GetFrame("func"), GetFrame("line")))

#if ... elif... else ...
color = "Red"
if color == "Red":
    print("Its Red + 1")
elif color == "Blue":
    print("Its Blue + 2")
else:
    print("Its Green + 3")

print("--------------------------------------------")

# in
a = 3
array1 = [1, 2, 3, 4, 5]
if a in array1:
    print("IN!!!")
else:
    print("NO!!!")

# False ... Anything else is considered True
"""
boolean         False
null            None
zero integer    0
zero float      0.0
empty string    ''
empty list      []
empty tuple     ()
empty dict      {}
empty set       set()
"""

print("--------------------------------------------")
# Repeat with while

count = 1
while count <= 5:
    print(count)
    count += 1

print("--------------------------------------------")
# Cancel with Break

while True:
    stuff = input("capitalize [q to quit]")
    if stuff == "q":
        break
    print(stuff.capitalize())

print("--------------------------------------------")
# Skip Ahead with continue

while True:
    value = input("Integer value [q to quit]")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is ", number * number)

print("--------------------------------------------")
# Check break Use with else

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number", number)
        break
    position += 1
else: # break not called
    print("No even number found!")

print("--------------------------------------------")
# Iterate with for
rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter'] 
for rabbit in rabbits:
    print(rabbit)
 
# String iteration produces a character at a time
word = "cat"
for letter in word:
    print(letter)

# Iterating over a dictionary (or its keys() function) returns the keys
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item) # print ('key name', 'item name')

for card, contents in accusation.items():
    print("Card", card, "Has the contents", contents) # Card room Has the contents ballroom

# Check break Use with else
#   If break was not called, the else statement is run.
#   This is useful when you want to verify that the previous for loop ran to completion,
#   instead of being stopped early with a break.
