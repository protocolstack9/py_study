#!/bin/python

"""If You're Having...
Let's get some practice with if statements. Remember, the syntax looks like this:

if some_function():
    # block line one
    # block line two
    # et cetera
Looking at the example above, in the event that some_function() returns True, then the indented block of code after it will be executed. In the event that it returns False, then the indented block will be skipped.

Also, make sure you notice the colons at the end of the if statement. We've added them for you, but they're important.
"""

def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print using_control_once()
print using_control_again()
