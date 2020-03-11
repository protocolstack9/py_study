##
## Name Mangling for Privacy
##
class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Donald'
print(fowl.name)

# cannot access by __name attribute
# fowl.__name

# This naming convention doesn’t make it private
print(fowl._Duck__name)
# ... didn’t print inside the getter
