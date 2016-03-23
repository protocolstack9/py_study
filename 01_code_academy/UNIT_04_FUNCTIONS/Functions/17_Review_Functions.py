#!/usr/bin/python

def shut_down(s):
    if (s == "yes"):
        return "Shutting down"
    elif (s == "no"):
        return "Shutdown aborted"
    else:
        return "Sorry"

print shut_down("yes")
