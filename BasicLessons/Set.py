"""Sets"""
#We can declare them two ways:
#x=set([1,2,3,4,5,6,7])
#x={1,2,3,4,5,6,7}

#Sets only admit one element. It is inmutable
# It can not repeat any element and can not be handle by indexes. We can not add list or dictionaries but touples
my_set=set({1,2,3,4,5})
print(type(my_set))

#We can add elements
my_set.add(6)

#We can remove or discards(safetly) elements
my_set.discard(2)
print(my_set)

#We can join multiple sets and it will automatically not consider repeated values
my_set2={2,5,6,7,8,9}
my_set3=my_set2.union(my_set)
print(my_set3)

print(5 in my_set)