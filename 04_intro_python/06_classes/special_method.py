##
## Special Methods --- surround with __
##
class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('AA')
second = Word('Aa')
third = Word('ca')

print(first.equals(second))
print(first.equals(third))

print(first == second)
print(first == third)

"""
Table 6-1. Magic methods for comparison
__eq__(self, other)         self == other
__ne__(self, other)         self != other
__lt__(self, other)         self < other
__gt__(self, other)         self > other
__le__(self, other)         self <= other
__ge__(self, other)         self >= other

Table 6-2. Magic methods for math
__add__(self, other)        self + other
__sub__(self, other)        self - other
__mul__(self, other)        self * other
__floordiv__(self, other)   self // other
__truediv__(self, other)    self / other
__mod__(self, other)        self % other
__pow__(self, other)        self ** other

Table 6-3. Other, miscellaneous magic methods
__str__(self)               str(self)
__repr__(self)              repr(self)
__len__(self)               len(self)
"""
