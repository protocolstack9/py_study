##
## Method Types --- instance method, @classmethod, @staticmethod
##
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", A.count, "little objects.")
#        print("A has", cls.count, "little objects.")

aa = A()
bb = A()
cc = A()
A.kids()


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

CoyoteWeapon.commercial()
