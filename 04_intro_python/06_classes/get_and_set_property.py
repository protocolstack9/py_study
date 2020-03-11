##
## Get and Set Attributes Values with Properties --- property()
##
print('-' * 20)

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
print(fowl.name)        # calling get_name()
print(fowl.get_name())

# @property, which goes before the getter method
# @name.setter, which goes before the setter method
"""
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
        
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
"""

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
"""
There’s one more big advantage of using a property over direct attribute access: if you ever change the definition of the attribute, you only need to fix the code within the class definition, not in all the callers.
"""
