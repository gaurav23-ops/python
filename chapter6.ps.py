#Q1 Write a program to find the greatest of four numbers entered by the user. 

d = int(input("Enter number d: "))
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if(a>b and a>c and a>d):
    print("A is greater number:-" , a)
elif(b>a and b>c and b>d):
    print("B is greater number:-" , b)
elif(c>a and c>b and c>d):
    print("C is greater number:-" , c)
else:
    print("D is greater number:-" , d)

print("end program")    


#Q2 Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

marks1 = int(input("Enter subject1 marks : "))
marks2 = int(input("Enter subject2 marks:  "))
marks3 = int(input("Enter subject3 marks:  "))

total_percentage = (marks1+marks2+marks3)/300*100
if(total_percentage>=40 and marks1>30 and marks2>33 and marks3>33):
    print("you passed" , total_percentage)

else:
    print("your failed" , total_percentage)    

#Q3 A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

message = input("write the message:- ")
if("make a lot money" == message or" buy now" == message or "subscribe this " == message or" click this" == message):
    print("This is spam by NASA ")
else:
    print("This is not spam by NASA")    

print("message is over")    

#Q4 Write a program to find whether a given username contains less than 10
# characters or not.

name = input("enter name less than 10 character:-")
names = len(name)<10
if(names):
    print("Good your are valid")
else:
    print("your not valid becz you have input is wrong no less than 10")    
    
#Q5 . Write a program which finds out whether a given name is present in a list or not

list = ("gaurav" , "sham ","sumit","sandesh", "akshay")
name = input("give name : ")
if(name in list):
    print("this name is in list")

else:
    print("this name in not in list")    

#Q6 Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

marks = int(input("give the marks"))
if( marks>=90 ):
    print("marks grade Execlent")
elif( marks>=80 ):
    print("marks grade A")
elif( marks>=70):
    print("marks grade B")
elif( marks>=60 ):
    print("marks grade C")
elif( marks>=50 ):
    print("marks grade D")
elif( marks<50 ):
    print("marks grade fail")



#Q7 Write a program to find out whether a given post is talking about “Harry” or not.

post = ("the harry is good buy but sometimr it not behave like good boy: ")
about = input("this post about who: ")
if(about in post):
    print("this post about harry ")
else:
    print("this post not about",about )  

print(" the program is end")    

