#!/bin/python

"""
Boolean operators aren't just evaluated from left to right. Just like with arithmetic operators, there's an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last.
For example, True or not False and False returns True. If this isn't clear, look at the Hint.

Parentheses () ensure your expressions are evaluated in the order you want. Anything in parentheses is evaluated as its own unit.
"""

# False or not True and True
bool_one = False

# False and not True or True
bool_two = True

# True and not (False or False)
bool_three = True

# not not True or False and not True
bool_four = True

# False or not (True and True)
bool_five = False
