# -*- coding: utf-8 -*-
#Python code to demonstrate working of iskeyword()
# importing "keyword" for keyword operations
import keyword
# printing all keywords at once using "kwlist()"
print ("The list of keywords is : ")
print (keyword.kwlist)
print("Hello World")
print("My name is Python and here is the list of keywords I understand")
j = 1
for i in keyword.kwlist:
    print ("The " + str(j) + "th keyword is " + i)
    j += 1
