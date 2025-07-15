#Q1  Write a python program to display a user entered name followed by Good
#Afternoon using input () function.

a = input("write your name:")
print("good afternoon ",a)

#Q2 Write a program to fill in a letter template given below with name and date
letter = '''
Dear <|gaurav|>,
You are selected!
<|15|07|>
'''
print(letter)

#Q3 Write a program to detect double space in a string.

gaurav = input("enter name: ")
print (gaurav.find(" "))

#Q4 Replace the double space from problem 3 with single spaces.
gaurav = input("enter name: ")
print(gaurav.replace("  "," "))

#Q5Write a program to format the following letter using escape sequence
#characters.
#letter = "Dear Harry, this python course is nice. Thanks!"
letter = "Dear Harry,\n\tthis python course is nice.\n Thanks!"
print(letter)

