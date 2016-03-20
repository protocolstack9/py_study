#!/bin/python

"""
Let's take a closer look at why you use len(string) and str(object), but dot notation (such as "String".upper()) for the rest.

lion = "roar"
len(lion)
lion.upper()
Methods that use dot notation only work with strings.
"""

ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()
