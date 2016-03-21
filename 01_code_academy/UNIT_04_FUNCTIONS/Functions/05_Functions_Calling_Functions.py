#!/usr/bin/python

"""
Functions Calling Functions
We've seen functions that can print text or do simple arithmetic, but functions can be much more powerful than that. For example, a function can call another function:

def fun_one(n):
    return n * 5

def fun_two(m):
    return fun_one(m) + 7
"""

def one_good_turn(n):
	return n + 1
    
def deserves_another(n):
	return one_good_turn(n) + 2


print deserves_another(10)
