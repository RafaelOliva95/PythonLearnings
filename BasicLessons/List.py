"""Lists"""
#List can store different types of variables, also list have other types of characteristics:
my_list=['a','b','c']
my_list2=['d','e','f']

#We can join two list together
my_list3=my_list+my_list2 
print(my_list3)     #[a,b,c,d,e,f]

#We can take different values with the indexes:
print(my_list[0:2]) #[a,b]

#We can replace a value with the index
my_list3[0]=1
print(my_list3)     #[1,a,b,c,d,e,f]

#We can add values using append
my_list3.append("final")
print(my_list3)     #[1,a,b,c,d,e,f,final]



#We can remove elements using pop
my_list3.pop() #pop will remove the last element if we don't specify the index
print(my_list3)     #[1,a,b,c,d,e,f]

#We can sort a list
my_list= ['c','b','g','f','a','d','e']
my_list.sort()
print(my_list)  #['a', 'b', 'c', 'd', 'e', 'f', 'g']

#We can invert the order
my_list.reverse()
print(my_list)      #['g', 'f', 'e', 'd', 'c', 'b', 'a']