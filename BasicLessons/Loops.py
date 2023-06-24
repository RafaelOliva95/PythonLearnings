my_list=['a','b','c','d']

#For each element in a data structure
for letter in my_list:
    index_of_letter=my_list.index(letter)   #Get the index of each letter
    print(f"Letter {index_of_letter}: "+ letter)

names=['juan','raul','ana','maria','carlos']
for name in names:
    print(f"{name} has {name.__len__()} letters")


#itarations in a list of lists
my_multilist=[['dog','cat'],['parrot','bird'],['fish','shark']]
for a,b in my_multilist:    #You can put two elements to print each of them in the structure of the array
    print(a)
    print(b)

#iterations in a dictonary 
my_dic={1:'a',2:'b',3:'c'}
for key in my_dic.items():      #without especifiying a property it will print the key values
    print(key)

