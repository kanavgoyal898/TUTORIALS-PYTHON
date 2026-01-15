# Property Decorators - Getters, Setters, and Deleters

# Property decorators, allow methods in a class to be accessed like attributes, providing a clean way to implement getters, setters, and deleters.

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
