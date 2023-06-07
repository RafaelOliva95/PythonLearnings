"""Dictionaries"""
#We have pairs on each field of the dictionary, one is for a key word and the second one, the value of that word
#They doesn't have an index or an specific order and the keywords can not be repeated

patient={'name':'Rafael','lastname':'Oliva','weight':95,'height':1.78}
print(patient['name'])  #Rafael

#We can add even dictionaries, list or other values in the value field
customers={ 1:{'name':'Amazon','address':'Denver','project':'Tech Refresh'},
            2:{'name':'Adidas','address':'Spartanburg','project':'Recontrol'},
            3:{'name':'TJX','address':'Phoenix','project':'System Expansion'}}
index=3
print('I have a {} for {} at {}'.format(customers[index]['project'],customers[index]['name'],customers[index]['address']))

#We can add another value or modified them with the key value
customers[4]={'name':'Michaels','address':'Chicago','project':'Scanners Upgrade'}

#We can also get all keys and values or items
print(patient.keys())
print(patient.values())
print(patient.items())