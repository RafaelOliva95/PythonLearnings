#Data types basics as any other language
#Python do not require to declare the variable typw
a=50        #int
b=5.5       #floats
c='c'       #char/string
d=True      #bool

#Data structures in Python
#List - Can contain any type of variable, they use an index
myList=["Rafael",27,500.58,"Oliva"]
#Dictionary - Grouped in pair of variables, it is use to access to values using the keys
myDic={"lastName":"Oliva","firstName":"Rafael","age":27}
#Tuples - Can contain any type of variables, but they can not change their order
myDays=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
#Sets - They can not repeat their elements
mySet= {'a','b','c','d','e'}

#note- You can print the type of a variable to know the type
#print(type(mySet))

#Exercises 1-Parsing
#myNumber=input("Dame un numero: ")
myNumber = 5.4
print(type(myNumber))
myNumber=int(myNumber)  #You can do parsing writting the type and inside '()' put the variable or value
print(type(myNumber))

#Exercise 2- Basic Operations
x=62
y=3
print(f"Addition {x}+{y} = {x+y}")
print(f"Subtraction {x}-{y} = {x-y}")
print(f"Multiplication {x}x{y} = {x*y}")
print(f"Division {x}/{y} = {x/y}")
print(f"Mod {x}%{y} = {x%y}")
print(f"Exponentiation {x}^{y} = {x**y}")
print(f"Square Root of {x}= {x**0.5}")
#Round to the previous integer
print(f"Round down {x}/{y} = {x//y}")
#Round and select the quantity of decimals
print(f"Round {x}/{y}={round(x/y,3)}")

#Project- Calculate the commission for a seller that get 13% of the ammount saled
name=input("What is your name: ")
sales= input("How much gain did you get: ")
sales=float(sales)
print(f"The commission for {name} is {round(sales*0.13,2)}")
