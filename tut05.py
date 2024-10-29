# Dictionaries - Working with Key-Value Pairs

me = {'firstName':'Kanav', 'lastName':'Goyal', 'age':18}
print(me)

# built-in functions
print(f"len(me): {len(me)}")

# dictionary methods
# get()
print(f"me.get('firstName') : {me.get('firstName')}")
print(f"me.get('middleName') : {me.get('middleName')}")
print(f"me.get('lastName', 'not-available') : {me.get('lastName', 'not-available')}")
# keys()
print(me.keys())
# values()
print(me.values())
# items()
print(me.items())
# pop()
print(f"me.pop('age') : {me.pop('age')}")
# update()
me.update({'courses':['CS-100, CS-200, CS-300, CS-400']})
print(me)

# loops
for key, value in me.items():
    print(f"{key} -> {value}")