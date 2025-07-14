#arithematic opretors (+ - * )
a = 1
b = 2
c = a+b
print(c)

# Assignment operators: =, +=, -= etc
b = 3
b += 6
print(b)

# Comparison operators: ==, >, >=, <, != etc.
a =5==5
print(a)
d = 5!=5
print(d)

# . Logical operators: and, or, not
# In 'or' only if false or false is false else true
# In 'and' only if true and true is true  else false 
# In Not(true)= false, Not(false) = true

print ("false or False is", False or False)
print ("True and true is", True and True)
print(not(True))

# type casting 
quit = 13
t=type(a)
print(t)


# There are many functions to convert one data type into another.
z = 12 
m = float(a)
t = type(b)
print(t)

# This function allows the user to take input from the keyboard as a string

a = int(input(" the number 1:"))
b = int(input(" the number 2:"))
print("number a is :",a)
print("number b is :",b)
print("sum is :", a + b)
