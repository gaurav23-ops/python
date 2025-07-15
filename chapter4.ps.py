#Q1 Write a program to store seven fruit in a list entered by the user
fruit=[]
f1 = input("enter the fruit:")
fruit.append(f1)
f2 = input("enter the fruit:")
fruit.append(f2)
f3 = input("enter the fruit:")
fruit.append(f3)
f4 = input("enter the fruit:")
fruit.append(f4)
f5 = input("enter the fruit:")
fruit.append(f5)
f6 = input("enter the fruit:")
fruit.append(f6)
f7 = input("enter the fruit:")
fruit.append(f7)
print(fruit)


#Q2 Write a program to accept marks of 6 students and display them in a sorted
# manner

marks=[]
f1 = input("enter the marks:")
marks.append(f1)
f2 = input("enter the marks:")
marks.append(f2)
f3 = input("enter the marks:")
marks.append(f3)
f4 = input("enter the marks:")
marks.append(f4)
f5 = input("enter the marks:")
marks.append(f5)
f6 = input("enter the marks:")
marks.append(f6)
f7 = input("enter the marks:")
marks.append(f7)
marks.sort()
print(marks)


#Q3 Check that a tuple type cannot be changed in python.
tuple = (1, 2 , 3)
print(tuple[0])
# tuple[0] = 0
# print(tuple)

#Q4 Write a program to sum a list with 4 numbers.

list = [1,2,5,3]

print(sum(list))

#Q5 Write a program to count the number of zeros in the following tuple:
#a = (7, 0, 8, 0, 0, 9) 
a = (7, 0, 8, 0, 0, 9) 
b=a.count(0)
print(b)

