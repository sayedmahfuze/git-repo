# Types of Variables 
"""
Python supports 2 types of variable 
1. Global Variables
2. Local Variables 

1. Global Variable 
The variabels which are declared outside of function are called global variables.
These variables can be accessed in all functions of that module.
"""
a = 10 
def f1():
	print(a)

def f2():
	print(a)


f1()
f2()
