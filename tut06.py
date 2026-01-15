# Conditionals and Booleans - If, Else, and Elif 

# False Values:
    # False
    # None
    # Zero of any numeric type.
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# if-else statements
if (True):
    print("Statement 1")
else:
    print("Statement 2")
if (False):
    print("Statement 1")
else:
    print("Statement 2")

# elif statements
if True:
    print("Statement 1")
elif True:
    print("Statement 2")
else:
    print("Statement 3")
if True:
    print("Statement 1")
elif False:
    print("Statement 2")
else:
    print("Statement 3")
if False:
    print("Statement 1")
elif True:
    print("Statement 2")
else:
    print("Statement 3")
if False:
    print("Statement 1")
elif False:
    print("Statement 2")
else:
    print("Statement 3")

# Boolean Operators
print(f"not T: {not True}")
print(f"not F: {not False}")
print(f"T and T : {True and True}")
print(f"T and F : {True and False}")
print(f"F and T : {False and True}")
print(f"F and F : {False and False}")
print(f"T or T : {True or True}")
print(f"T or F : {True or False}")
print(f"F or T : {False or True}")
print(f"F or F : {False or False}")

# 'is' operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 == list2 : {list1 == list2}")
print(f"list1 is list2 : {list1 is list2}")
print(f"id(list1) == id(list2) : {id(list1) == id(list2)}")
