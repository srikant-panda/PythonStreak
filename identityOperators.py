'''
Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
Operator 	Description 	   Example 	   Try it
is  	Returns True if both   variablesare the same object	
is not 	Returns True if both   variablesare not the same object  	

'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)