#!/bin/python

"""
Else Problems, I Feel Bad for You, Son...
The else statement complements the if statement. An if/else pair says: "If this expression is true, run this indented code block; otherwise, run this code after the else statement."

Unlike if, else doesn't depend on an expression. For example:

if 8 > 9:
    print "I don't printed!"
else:
    print "I get printed!"
"""

answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False       # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False

print black_knight()
print french_soldier()
