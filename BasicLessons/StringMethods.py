#We will use here some of the common methods for strings
text = "This Is My Text Example That Will Help Me To Run Some Tests"
#Upper - Transform characters to upper
result=text.upper()
print(result)
#Lower - Transform all characters to lower
result=text.lower()
print(result)
#Split - it will separate my string into pices inside a list, we can specify a parameter to use instead of spaces
result=text.split()
print(result)
#Join - It will merge strings in one we can specify a separator at the beginning
textJoinned=" ".join(["learn","python","is","great"])
print(textJoinned)
#Replace - It will replace an specified string to another one
textJoinned=textJoinned.replace("python","java")
print(textJoinned)

#Look for an string in another string an save it in a boolean
contain="java"in textJoinned
print(contain)

#Len- Know the amount of characters in an string
print(len(textJoinned))