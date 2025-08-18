#Q1.Create a list of 5 integers. Print the sum of all elements.

# number =[10,10,10,10,10]
# total = sum(number)
# print("sum of num",total)

#Q2.Input 10 numbers from the user and store them in a list.

# n = int(input("enter num 1:"))
# n1 = int(input("enter num 2:"))
# n2 = int(input("enter num 3:"))
# n3 = int(input("enter num 4:"))
# n4 = int(input("enter num 5:"))
# n5 = int(input("enter num 6:"))
# n6 = int(input("enter num 7:"))
# n7 = int(input("enter num 8:"))
# n8 = int(input("enter num 9:"))
# n9 = int(input("enter num 10:"))
# print([n,n1,n2,n3,n4,n5,n6,n7,n8,n9])


#Q3.Write a program to find the maximum and minimum in a list.

# num = [1,2,3,4,5,6]
# print(max(num),min(num))

#Q4.Remove all even numbers from a given list.

# even = [1,2,3,4,5,6,7,8]
# n = [num for num in even if num % 2 != 0]
# print(n)

#Q5.Reverse a list without using reverse() method.

# num = [1,2,3,4,5,6,7]
# d = num [ ::-1]
# print(d)

#Q7.Count the occurrences of a particular element in a list.

n1 =[1,1,1,2,3,2,3,2,1,2,2,4,1,2]
d = n1.count(2)
print(d)

#Q8.Write a program to remove duplicates from a list.

n2 = [1,2,3,1,2,3,1,2,3,5,2,6,4]
s = list(set(n2))
print(s)

#Q9.Merge two lists into one.
n3 = [1,2,3]
n4 = [4,5,6]
q = [n3+n4]
print(q)


#Q10.Write a program to swap the first and last elements in a list.

n5 = [1,2,3,4,5,6]
n5[0],n5[5]=n5[5],n5[0]
print(n5)

#Q11.Create a list of squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)


#Q13.Find the second largest number in a list.
n7 = [1,2,3,4,5,6]
n7.sort()
d = n7[-2]
print(d)

#Q14.Copy all elements from one list to another.
n7 = [1,2,3,4,5,6]
n8 = n7
print(n7)
print(n8)

#Q15.Check if a list is a palindrome (same forwards and backwards).