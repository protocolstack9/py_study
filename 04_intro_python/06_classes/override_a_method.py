class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person): # inherite
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person): # inherite
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')

print(person.name)
print(doctor.name)
print(lawyer.name)


##
## Get Help from Your Parent with super --- super()
##

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

mailman = EmailPerson('mailman', "a@b.com")
print(mailman.name, ", ", mailman.email)
