# Special Dunder Methods

class ClassName:
    def __init__(self, propertyA, propertyB):
        self.propertyA = propertyA
        self.propertyB = propertyB
    def __repr__(self):
        return f'ClassName({self.propertyA}, {self.propertyB})'
    def __str__(self):
        return f'{self.propertyA} - {self.propertyB}'
    
instanceName = ClassName(0, 1)
print(instanceName)