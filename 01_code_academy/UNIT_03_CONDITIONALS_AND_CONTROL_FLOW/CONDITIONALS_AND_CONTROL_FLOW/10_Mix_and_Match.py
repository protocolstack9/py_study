#!/bin/python

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = not ((2 <= 2) and "Alpha" == "Bravo")

# Make me false!
bool_three = not not ((2 <= 2) and "Alpha" == "Bravo")

# Make me true!
bool_four = not not not ((2 <= 2) and "Alpha" == "Bravo")

# Make me true!
bool_five = not not not ((2 <= 2) and "Alpha" == "Bravo")

print "%s %s %s %s %s" % (bool_one, bool_two, bool_three, bool_four, bool_five)
