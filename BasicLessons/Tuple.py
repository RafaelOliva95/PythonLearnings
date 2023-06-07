"""Tupples"""
#Tupples are pretty similar to lists bur they are inmutable that means that we can not modify them
#As lists we can use inside them any type of varibles
my_tuple=(1,2.5,'c',"four",['a','b','c'])
print(type(my_tuple))

#We can use indexes
print(my_tuple[4])

#We can convert touples into list
my_tuple=list(my_tuple)
print(type(my_tuple))

#We can also count the amount of types an element appears
my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)
print(my_tuple.count(2))
