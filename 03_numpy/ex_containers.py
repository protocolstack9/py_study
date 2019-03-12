print("---------------------------------------")
print(" Containers ");
print("---------------------------------------")

""" Lists """

xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1]) # count from end of the list - '2'
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop() # from last element
print(x, xs)


""" Slicing """
nums = list(range(5))   # 0 to 4
print(nums)
print(nums[2:4]) # 2:4(exclusive)
print(nums[2:])
print(nums[:])
print(nums[:2])
print(nums[:-1])
nums[2:4] = [8, 9]
print(nums)


""" Loops """
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)

for idx, animal in enumerate(animals):
    print("#%d: %s" % (idx+1, animal))

""" List comprehensions """
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

squares = [x ** 2 for x in nums]
print(squares)

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)



""" dictionary """

d = {'cat': "cute", 'dog': "furry"}
print(d['cat'])

print('cat' in d) # Check if a dictionary has a given key....
d['fish'] = "wet"
print(d['fish'])

print(d.get('monkey', 'N/A'))
print(d.get('fish', 'N/A'))
del d['fish']
print(d.get('fish', 'N/A'))



""" Loop """
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print("A %s has %d legs" % (animal, legs))

for animal, legs in d.items():
    print("A %s has %d legs" % (animal, legs))



""" Dictionary comprehensions """
nums = list(range(5)) # [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)



""" sets """
animals = {'cat', 'dog'}
print('cat' in animals)
print('fish' in animals)    # True or False
animals.add('fish')         # 'add'
print('fish' in animals)
print(len(animals))
animals.add('cat')          # already in the set does nothing
print(len(animals))
animals.remove('cat')       # 'remove'
print(len(animals))

""" Loops """
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print("#%d: %s" % (idx+1, animal))



""" set comprehensions """
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)



""" Tuples """
d = {(x, x+1): x for x in range(10)}
t = (5, 6)
print(type(t))  # <class 'tuple'>
print(d[t])
print(d[(1,2)])
