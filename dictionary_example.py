#Q1.Create a dictionary of 3 students and their marks. Print all keys and values.
s = {'gaurav':30 , 'sham':86, 'sumit':89}
print(s)

#Q2.Add a new key-value pair to the dictionary.
s = {'gaurav':30 , 'sham':86, 'sumit':89}
s['grade'] = 'a'
print(s)

#Q3.	Update the marks of a student in the dictionary.
s = {'gaurav':30 , 'sham':86, 'sumit':89}
d = s.update({'sandesh':89})
print(s)

#Q4.Remove a key from a dictionary using pop().
s = {'gaurav':30 , 'sham':86, 'sumit':89}
d = s.pop('gaurav')
print(s)

#Q5.Create a dictionary from two lists: one of keys, one of values.
key = ['gaurav','sham','sumit']
value = [86,74,85]
h= dict(zip(key, value))
print(h)

#Q6.Count the frequency of each character in a string using dictionary.
# g = "gaurav"
# v = dict(counter(g))
# print(v)

#Q7.	Merge two dictionaries into one.
s = {'gaurav':30,'sham':50}
d = {'sumit':20}
g = s,d
print(g)

#Q8.	Check if a key exists in a dictionary.
s = {'gaurav':30,'sham':50}
f=('gaurav')
g = (f in s)
print(g)

#Q10.Get value using .get() method (with and without default).

s = {'gaurav':30,'sham':50}
d = s.get('gaurav')
print(d)

#Q11.Create a nested dictionary for student with name, age, and marks.
student = {'student1':
           {'name':'gaurav', 'age':20 ,
             'marks':
             {'science':70,'math':84,'english':74
              }
              },
           'student2':
           {'name':'sham', 'age':20 , 
            'marks':
            {'science':88,'math':85,'english':71
             }
            }
            }
print("gaurav marks of science" ,student['student1']['marks']['science'])
print("sham marks of science" ,student['student2']['marks']['science'])

#Q12.	Sort a dictionary by its values.

# s = {'gaurav':96 , 'sham':86, 'sumit':89}
# d = dict(sorted(s.values()))
# print(d)

#Q13.	Find the key with the maximum value in a dictionary.
s = {'gaurav':96 , 'sham':86, 'sumit':89}
print(max(s))

#Q14.	Convert a dictionary into a list of tuples (key, value).

s = {'gaurav':96 , 'sham':86, 'sumit':89}
f = tuple(key)
d = tuple(value)
x = f,d
print(x)

#Q15.	Write a program that takes a sentence and returns a dictionary of word counts.

s = input("enter sentence")
print(s)
x = dict(s[key,value])
print(x)
