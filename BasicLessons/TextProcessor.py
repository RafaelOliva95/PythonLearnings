# Understand the basic of an string
"""Each character has it's own index in an string
In the string: "Hello World" it has 11 characters and these are their index:
Character         Index
    H       -       0
    E       -       1
    L       -       2
    L       -       3
    O       -       4
            -       5
    W       -       6
    O       -       7
    R       -       8
    L       -       9
    D       -       10
"""
# Practice: Create a string and look for the index of a specific letter
#           then print the index number 3 of that string
myString="I'm learning Python"
print(myString[6])
#String can also use negative index
"""Character         Index
    H       -       0
    E       -       -10
    L       -       -9
    L       -       -8
    O       -       -7
            -       -6
    W       -       -5
    O       -       -4
    R       -       -3
    L       -       -2
    D       -       -1
"""
print(myString[-11])