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

#We can also specify parameters like start 
result=myString.index("n",9,15) #it will start looking n from index 9 to 15
print(result)

result=myString.rindex("n",9) #rindex will start looking from right to left
print(result)

""" Slicing:
It can help us to create substrings 
myString[start_index:end_index:jumps] 
We can avoid them some of them 
In the case we avoid start_index it will start from the beginning
If we avoid end_index it will finish at the very end
If we don't put a jump it will do it one by one
*Note: If we put a negative jump it will do it from right to left
 """
myString="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(myString[5:])     #We print from index 5 to the end
print(myString[5:10])   #We print from index 5 to 10
print(myString[5:15:2]) #We print from index 5 to 10 every 2 characters
print(myString[::-1])   #We print string backwards

