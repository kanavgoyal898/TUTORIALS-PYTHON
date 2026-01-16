# Using Try/Except Blocks for Error Handling

# try: Wraps code that may raise an exception.
# except: Catches and handles exceptions raised in the try block.
# else: Runs only if the try block completes without any exception.
# finally: Always executes, regardless of whether an exception occurred or not.

try:
    f = open("sample.txt")
except Exception:
    print("An unexpected error occurred.")

try:
    f = open("sample.txt")
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(e)

print()

try:
    message = "hello, world"
except Exception as e:
    print(e)
else:
    print(message)
    print("Else block: No errors occurred.")
finally:
    print("Finally block: Execution completed.")

print()

try:
    f = open("sample.txt")
    if f.name == "sample.txt":
        raise Exception
except Exception:
    print("Manual exception raised.")
