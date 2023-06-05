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
#           then print the index number 6 of that string
myString="I'm learning Python"
print(myString[6]) #It will print 'a'
#String can also use negative index
"""Character   Index negative     Index positive
    I       -       0                   0
    '       -       -18                 1
    m       -       -17                 2
            -       -16                 3
    l       -       -15                 4
    e       -       -14                 5
    a       -       -13                 6
    r       -       -12                 7
    n       -       -11                 8
    i       -       -10                 9
    n       -       -9                  10
    g       -       -8                  11
            -       -7                  12
    P       -       -6                  13
    y       -       -5                  14
    t       -       -4                  15
    h       -       -3                  16
    o       -       -2                  17
    n       -       -1                  18
"""
print(myString[-11]) #We will print 'n'

#We also can find strings inside strings
result=myString.index("Python") #Python start at index 13
print(result)