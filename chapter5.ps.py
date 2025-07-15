
#Q1 Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
dict={"panni":"water",
      "keli":"banana", 
      "dhud":"milk"}
a = input("enter the hindi word:")
print(dict.get(a, "Word not found in dictionary."))

#Q2 Write a program to input eight numbers from the user and display all the unique
# numbers (once).

a = input("enter 8 number ")
b= a.split()
c = [int(x) for x in b] 
set = set(c)
print(set)

#Q3 Can we have a set with 18 (int) and '18' (str) as a value in it?
s1={18 , '18'}
print(s1 , type(s1))


#Q4 What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))


#Q5  s = {}
# What is the type of 's'?
#my answer it type is dict 

s = {}
print(type(s))

#Q6 Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

fav_lan = {}
name1 = input("enter the name")
lang1 = input("enter the language")
fav_lan[name1] = lang1

name2 = input("enter the name")
lang2 = input("enter the language")
fav_lan[name2] = lang2 

name3 = input("enter the name")
lang3 = input("enter the language")
fav_lan[name3] = lang3 

name4 = input("enter the name")
lang4 = input("enter the language")
fav_lan[name4] = lang4 
print(fav_lan)

#Q7 If the names of 2 friends are same; what will happen to the program in problem
# 6?

#nothing will happen because names same but value are different 


#Q8 If languages of two friends are same; what will happen to the program in problem

#ans- No problem at all!
# Python dictionaries allow duplicate values — it's only the keys (names) that must be unique.


#Q9 Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]}
print(s)
