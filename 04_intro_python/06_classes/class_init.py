class Person():
    def __init__(self, name):
        self.name = name

class Nothing():
    def __init__(self):
        pass

a_man = Person('John Doe')
anonymous = Nothing()

print(a_man.name)
