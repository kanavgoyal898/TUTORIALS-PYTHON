# Lists, Tuples & Sets

# In Python, immutability means that an object's value or state cannot be changed after it is created. Any operation that appears to modify an immutable object actually creates a new object in memory, and the variable name is then reassigned to reference this new object.

# Lists - Mutable Data Collection Type
emptyList = list()      # or []
print(emptyList)
characters = ["Harry Potter", "Hermione Granger", "Ron Weasley"]
print(characters)

print(f"characters[0]  : {characters[0]}")
print(f"characters[-1] : {characters[-1]}")

print(f"Voldemort in characters? : {'Voldemort' in characters}")

# loops
for character in characters:
    print(character)
# 0-indexing
for index, character in enumerate(characters):
    print(index, character)
# n-indexing
for index, character in enumerate(characters, start = 3):
    print(index, character)

# join() & split() methods
listToStr = ' - '.join(characters)
print(f"type(listToStr): {type(listToStr)}")
strToList = listToStr.split(' - ')
print(f"type(strToList): {type(strToList)}")

# Lists - built-in functions
# len()
print(f"len(characters) : {len(characters)}")
# min()
print(f"min([1, 2, 3, 4, 5]): {min([1, 2, 3, 4, 5])}")
# max()
print(f"max([1, 2, 3, 4, 5]): {max([1, 2, 3, 4, 5])}")
# sum()
print(f"sum([1, 2, 3, 4, 5]): {sum([1, 2, 3, 4, 5])}")
# sorted()
characters_sorted = sorted(characters)
print(f"characters_sorted <Ascending Order>:  {characters_sorted}")
characters_sorted = sorted(characters, reverse = True)
print(f"characters_sorted <Descending Order>: {characters_sorted}")

# Lists - built-in methods (in-place operations)
# append()
characters.append('Neville Longbottom')
print(f"characters - append('Neville Longbottom') : {characters}")
# insert()
characters.insert(3, 'Ginny Weasley')
print(f"characters - insert(3, 'Ginny Weasley') : {characters}")
# extend()
characters.extend(['Prof. Albus Dumbledore', 'Prof. Severus Snape', 'Prof. Minerva McGonagall', 'Hagrid'])
print(f"characters - extend(['Prof. Albus Dumbledore', 'Prof. Severus Snape', 'Prof. Minerva McGonagall', 'Hagrid']) : {characters}")
# remove()
characters.remove('Ginny Weasley')
print(f"characters - remove('Ginny Weasley') : {characters}")
# pop()
print(f"characters.pop(): {characters.pop()}")
print(f"characters: {characters}")
# reverse()
characters.reverse()
print(f"characters - reverse(): {characters}")
characters.reverse()
print(f"characters - reverse(): {characters}")
# find()
print(f"characters.index('Harry Potter') = {characters.index('Harry Potter')}")
# sort()
characters.sort()
print(f"characters - sort() <Ascending Order>: {characters}")
characters.sort(reverse = True)
print(f"characters - sort(reverse = True) <Descending Order>: {characters}")


# Tuples - Immutable Data Collection Type
emptyTuple = tuple()        # or ()
print(emptyTuple)
houses = ('Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin')
print(houses)


# Sets - Unordered Data Collection Type
emptySet = set()
print(emptySet)
character_set1 = {'Harry', 'Hermione', 'Ron'}
character_set2 = {'Neville', 'Ginny', 'Draco'}
print(character_set1, character_set2)
print(f"character_set1.union(character_set2) : {character_set1.union(character_set2)}")
print(f"character_set1.intersection(character_set2) : {character_set1.intersection(character_set2)}")
print(f"character_set1.difference(character_set2) : {character_set1.difference(character_set2)}")
print(f"character_set2.difference(character_set1) : {character_set2.difference(character_set1)}")
