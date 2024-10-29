# Functions

# non-parameterized functions
def helloGreeting():
    return 'Hello World'
print(f"helloGreeting: {helloGreeting}")
print(f"helloGreeting(): {helloGreeting()}")

# parameterized functions
def customGreeting(greeting, name = 'World'):
    return f'{greeting}, {name}'
print(f"customGreeting: {customGreeting}")
print(f"customGreeting('Hello'): {customGreeting('Hello')}")
print(f"customGreeting('Hello', 'World'): {customGreeting('Hello', 'World')}")

# positional keyword arguments
def info(*args, **kwargs):
    # args: tuple
    print(args)
    # kwargs: dict
    print(kwargs)
info('Physics', 'Chemistry', 'Mathematics', p = 1, c = 2, m = 3)
subjects = ['Physics', 'Chemistry', 'Mathematics']
priority = {'p' : 1, 'c' : 2, 'm' : 3}
info(*subjects, **priority)