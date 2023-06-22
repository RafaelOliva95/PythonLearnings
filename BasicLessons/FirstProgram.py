#Here I'm placing the basic commands and variable declaration in python

#My first string
print("Hello World")

#First variables
firstName = 'Rafael'
lastName = 'Oliva'
age= 27     #python automatically detect the type of variable

# print variables using 'f' before the text and place the variables inside keys {}

print(f"Hello Mr. {lastName}")
print(f"{firstName} has {age} years old")

#Users can insert text using input
favoriteColor = input("Please insert your favorite color: ")
print(F"Mr. {lastName} favorite color is {favoriteColor}")

#Exercise
#Create a program to create your beer branch name
print("Your beer name could be: "+favoriteColor+lastName)

#Format- Print variables
print(f"Your beer name could be: {favoriteColor}{lastName}")
print("Your beer name could be: {}{}".format(favoriteColor,lastName))

#Project- Calculate the commission for a seller that get 13% of the ammount saled
name=input("What is your name: ")
sales= input("How much gain did you get: ")
sales=float(sales)
print(f"The commission for {name} is {round(sales*0.13,2)}")
