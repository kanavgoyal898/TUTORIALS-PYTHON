# Loops and Iterations - For/While Loops

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# break:
# Immediately terminates the loop and transfers control to the first statement after the loop.

# continue:
# Skips the rest of the current iteration and jumps to the next iteration of the loop.

# for loop
for i in range(3):
    print(i)

# nested for loops
for x in range(1, 4):
    for y in range(1, 4):
        print(x, y)

# while loop
x = 1
while True:
    print(x)
    x += 1
    if x > 3:
        break
    else:
        continue
    