# Special (Magic/Dunder) Methods

class ClassName:

    def __init__(self, propertyA, propertyB):
        self.propertyA = propertyA
        self.propertyB = propertyB

    def __repr__(self):
        # fallback for __str__()
        return f'ClassName({self.propertyA}, {self.propertyB})'
    
    def __str__(self):
        return f'{self.propertyA} - {self.propertyB}'
    
instanceName = ClassName(0, 1)

print(repr(instanceName))
print(str(instanceName))

print(instanceName.__repr__())
print(instanceName.__str__())

print(instanceName)

print(int.__add__(0, 1))
print(str.__add__('hello, ', 'world'))
print(list.__len__([1, 2, 3, 4, 5]))
