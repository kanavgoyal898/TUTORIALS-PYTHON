# Decorators - Dynamically Alter The Functionality Of Your Functions

# First-order functions:
# First-order functions are functions that are treated like any other value in Python: they can be assigned to variables, stored in data structures, passed as arguments, and returned from other functions.

# Closures:
# A closure in Python is created when an inner function captures and retains access to variables from its enclosing (outer) function even after that outer function has finished executing. This lets the inner function carry state with it without using globals or classes, because the captured variables are stored in the function’s environment.

def outer_function(message):
    def inner_function():
        print(message)
    return inner_function

closure_1 = outer_function("Hi, World!")
closure_1()

closure_2 = outer_function("Bye, World!")
closure_2()

print()

# Decorators exist to let you modify or extend a function’s behavior without changing its source code. They work by wrapping a function with another function (via closures and first-class functions), so you can inject logic before and/or after the original call—like logging, timing, caching, authentication, validation, or retrying—while keeping the core function clean and focused on its job.

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(original_function.__name__))
        x = original_function()
        print("Wrapper executed this after {}".format(original_function.__name__))
        return x
    return wrapper_function

# Method 1: Manually decorating a function

def original_function_1():
    print("This is the original function 1.")

original_function_1 = decorator_function(original_function_1)
print(f"Function name: {original_function_1.__name__}")
original_function_1()
print()

# Method 2: Using the @ syntax

@decorator_function
def original_function_2():
    print("This is the original function 2.")

print(f"Function name: {original_function_2.__name__}")
original_function_2()
print()

# Decorators with arguments

def decorator_function_with_args(original_function):
    def wrapper_function_with_args(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        x = original_function(*args, **kwargs)
        print("Wrapper executed this after {}".format(original_function.__name__))
        return x
    return wrapper_function_with_args

@decorator_function_with_args
def original_function_with_args(a, b):
    print("This is the original function with args: {}, {}".format(a, b))

original_function_with_args(0, 1)
print()

# Class decorators

class DecoratorClass:
    
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Class Wrapper executed this before {}".format(self.original_function.__name__))
        x = self.original_function(*args, **kwargs)
        print("Class Wrapper executed this after {}".format(self.original_function.__name__))
        return x
    
@DecoratorClass
def original_function_class_decorator(a, b):
    print("This is the original function with class decorator: {}, {}".format(a, b))

original_function_class_decorator(0, 1)
print()

# Practical Decorators

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    
    return wrapper

@my_logger
def display(greeting, name):
    return '{}, {}!'.format(greeting, name)

display('Hello', 'John')
display('Hello', 'Jane')
print()

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time()
        dt = t2 - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, dt))
        return result
    
    return wrapper

@my_timer
def display_(greeting, name):
    return '{}, {}!'.format(greeting, name)

display_('Hi', 'John')
display_('Hi', 'Jane')
print()

# Using functools.wraps to preserve metadata

from functools import wraps

def decorator_with_wraps(original_function):
    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        x = original_function(*args, **kwargs)
        print("Wrapper executed this after {}".format(original_function.__name__))
        return x
    return wrapper_function

@decorator_with_wraps
def original_function_with_wraps(a, b):
    print("This is the original function with wraps: {}, {}".format(a, b))

original_function_with_wraps(0, 1)
print(f"Function name: {original_function_with_wraps.__name__}")

# Decorator chaining

# @decorator_A
# @decorator_B
# @decorator_C
# def original_function_chained():
#     print("This is the original function with chained decorators.")

# def original_function_chained():
#     print("This is the original function with chained decorators.")
# original_function_chained = decorator_A(decorator_B(decorator_C(original_function_chained)))
# original_function_chained()
