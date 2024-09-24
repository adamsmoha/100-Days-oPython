# for loops: are used when you know the exact number of iterations.

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

for fruit in fruits:
    print(fruit)

# range(): generates a sequence of numbers, which can be used in loops, lists,
# and other data structures. Think of it like a counter that starts from a
# specific number and stops at another specific number.

# range(start, stop, step)

for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(0, 10, 2):
    print(i)

# while loop: are used when you don't know the exact number of iterations.

i = 0
while i < 5:
    print(i)
    i += 1
