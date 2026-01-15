# Inheritance - Creating Subclasses

class PeriodicTable:

    totalElements = 118

    def __init__(self, groups = 18, periods = 7):
        self.groups = groups
        self.periods = periods

    def description(self):
        print(f"Total Elements: {self.totalElements}")

class _Block(PeriodicTable):
    pass
        
class sBlock(PeriodicTable):

    totalElements = 14

    def __init__(self, groups, periods, groupRange):
        super().__init__(groups, periods)
        self.groupRange = groupRange

class pBlock(PeriodicTable):

    totalElements = 35

    def __init__(self, groups, periods, groupRange):
        super().__init__(groups, periods)
        self.groupRange = groupRange

class dBlock(PeriodicTable):

    totalElements = 40

    def __init__(self, groups, periods, groupRange):
        super().__init__(groups, periods)
        self.groupRange = groupRange

class fBlock(PeriodicTable):

    totalElements = 30

    def __init__(self, groups, periods, groupRange):
        PeriodicTable.__init__(self, groups, periods)
        self.groupRange = groupRange

_block = _Block()
_block.description()

print(help(_block))

sblock = sBlock(18, 7, [1, 2])
pblock = pBlock(18, 7, [13, 14, 15, 16, 17, 18])
dblock = dBlock(18, 7, [3, 4, 5, 6, 7, 8, 9, 10])
fblock = fBlock(18, 7, [3])

sblock.description()
pblock.description()
dblock.description()
fblock.description()

print(f"isinstance(sblock, PeriodicTable) : {isinstance(sblock, PeriodicTable)}")
print(f"isinstance(sblock, sBlock) : {isinstance(sblock, sBlock)}")

print(f"isinstance(pblock, PeriodicTable) : {isinstance(pblock, PeriodicTable)}")
print(f"isinstance(pblock, pBlock) : {isinstance(pblock, pBlock)}")

print(f"isinstance(dblock, PeriodicTable) : {isinstance(dblock, PeriodicTable)}")
print(f"isinstance(dblock, dBlock) : {isinstance(dblock, dBlock)}")

print(f"isinstance(fblock, PeriodicTable) : {isinstance(fblock, PeriodicTable)}")
print(f"isinstance(fblock, fBlock) : {isinstance(fblock, fBlock)}")

print(f"issubclass(sBlock, PeriodicTable) : {issubclass(sBlock, PeriodicTable)}")
print(f"issubclass(pBlock, PeriodicTable) : {issubclass(pBlock, PeriodicTable)}")
print(f"issubclass(dBlock, PeriodicTable) : {issubclass(dBlock, PeriodicTable)}")
print(f"issubclass(fBlock, PeriodicTable) : {issubclass(fBlock, PeriodicTable)}")
