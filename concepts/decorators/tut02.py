# Decorators With Arguments

def decorator_function_with_args(arg):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(arg, "Wrapper executed this before {}".format(original_function.__name__))
            x = original_function(*args, **kwargs)
            print(arg, "Wrapper executed this after {}".format(original_function.__name__))
            return x
        return wrapper_function
    return decorator_function

@decorator_function_with_args("LOG:")
def original_function_with_args(a, b):
    print("This is the original function with args: {}, {}".format(a, b))

original_function_with_args(0, 1)
print()
