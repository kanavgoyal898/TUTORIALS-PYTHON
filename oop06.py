# Property Decorators - Getters, Setters, and Deleters

class Me:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    @property
    def fullName(self):
        return self.firstName + " " + self.lastName
    @fullName.setter
    def fullName(self, str):
        self.firstName, self.lastName = str.split(' ')
    @fullName.deleter
    def fullName(self):
        self.firstName = None
        self.lastName = None
    
person = Me('John', 'Doe')
print(person.fullName)

person.fullName = 'Jane Doe'
print(person.fullName)

del person.fullName