#!/usr/bin/python

import types
def distance_from_zero(arg):
    if (type(arg) == types.IntType or type(arg) == types.FloatType):
        return abs(arg)
    else:
        return "Nope"

print distance_from_zero(20)
