#Q1.Create a tuple of 5 numbers and print their sum.
num = (1,2,3,4,5)
f = sum(num)
print(sum)

#Q2.Write a function that returns max and min from a tuple.

num = (1,2,3,4,5)
f = max(num), min(num)
print(sum)

#Q4.Create a tuple of 5 strings and print them in reverse order.
num = (1,2,3,4,5)
s = num[::-1]
print(s)

#Q3.	Convert a list to a tuple and vice versa.

num = [1,2,3,4]
s = tuple(num)
print(s)
d = (1,2,3,4)
a = list[d]
print(a)

#Q5.	Count how many times a specific element appears in a tuple.

d = (1,2,3,4,1,2,3,4,4)
b = d.count(4)
print(b)

#Q6.	Find the index of an element in a tuple.

f = (1,2,3,4,5,6)
s = f.index(1)
print(s)


#Q7.	Check if a value exists in a tuple.
f = (1,2,3,4,5,6)
print(3 in f)

#Q8.	Concatenate two tuples.

f = (1,2,3)
s = (4,5,6)

print(s,f)

#Q9.	Slice a tuple to get only the middle 3 elements.
f = (1,2,3,4,5,6,7,8,9)
s = f[3:6:]
print(s)

#Q10.	Unpack a tuple of 3 values into separate variables.
f = (1,2,3)
a , b , c = f
print(a)
print(b)
print(c)

#Q11.	Create a tuple containing another tuple.

f =(1,2,3,4,5,(4,5,6,7,8,9))
print(f)

#Q12.	Write a function that accepts a tuple of numbers and returns their average.
s = (1,2,3,4,5,6,7,8,9)
a = sum(s)
print(a)
print(a/len(s))

#Q13.Make a tuple of vowels from a given string.

s = ('aajeyd')
d = tuple(s)
print(d)

#Q14.	Sort a tuple of numbers.

s = (1,3,2,5,4,)
d = tuple(sorted(s))
print(d)

#Q15.Write a program to check if all items in a tuple are the same.
s = (1,2,3,4,5,6,7,8,9)

