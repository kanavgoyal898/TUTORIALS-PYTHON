# Context Managers - Efficiently Managing Resources

f = open("sample.txt", "w")
f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
f.close()

with open("sample_.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

# Context Manager using classes

class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # Setup actions
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Teardown actions
        self.file.close()

with OpenFile("sample_1.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

print("File closed successfully?", f.closed)

# Context Manager using functions

from contextlib import contextmanager

@contextmanager
def openFile(filename, mode):
    try:
        # Setup actions
        f = open(filename, mode)
        yield f
    finally:
        # Teardown actions
        f.close()

with openFile("sample_2.txt", "w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

print("File closed successfully?", f.closed)

# Example: Change Directory Context Manager

# Method 1: Without Context Manager

import os

def change_dir(destination):
    cwd = os.getcwd()
    print("Current Directory:", cwd)
    os.chdir(destination)
    print("Current Directory:", os.getcwd())
    print(f"Contents of {destination}: {os.listdir()}")
    os.chdir(cwd)
    print("Current Directory:", os.getcwd())

change_dir("dir_1")
change_dir("dir_2")

# Method 2: With Context Manager

import os
from contextlib import contextmanager

@contextmanager
def change_directory(destination):
    try:
        cwd = os.getcwd()
        print("Current Directory:", cwd)
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
        print("Current Directory:", os.getcwd())

with change_directory("dir_1"):
    print("Current Directory:", os.getcwd())
    print(f"Contents of dir_1: {os.listdir()}")

with change_directory("dir_2"):
    print("Current Directory:", os.getcwd())
    print(f"Contents of dir_2: {os.listdir()}")
