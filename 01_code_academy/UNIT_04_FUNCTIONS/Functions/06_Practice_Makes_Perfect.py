#!/usr/bin/python

"""
Practice Makes Perfect
Let's create a few more functions just for good measure.

def shout(phrase):
    if phrase == phrase.upper():
        return "YOU'RE SHOUTING!"
    else:
        return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")
The example above is just there to help you remember how functions are structured.

Don't forget the colon at the end of your function definition!
"""

def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print by_three(3)
