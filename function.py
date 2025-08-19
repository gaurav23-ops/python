# def hello(*name):
#     print("hello , my name is ",name[1])
# hello("gaurav","sham")

# def a (s,d,f):
#     if s > d and s > f:
#         print("is greatest",s)
#     elif d>s and d>f:
#         print("d is greatest",d)
#     else:
#         print("f is greatest",f)              
# a(2,5,4)

# def creat_list():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)

#     return(l)
# print(creat_list())    


# def check_prime(num):
#     if num == 1:
#         print("its not prime numnber")
#     if num == 2:
#         print("its  prime numnber")
#     for i in range(2 , num):
#         if num % i == 0:
#             print("print its not prime")
#             break
#     else:
#         print("its print numnber")
# check_prime(5)                

def add(num):
    total = 0
    for i in num:
        total += i
    return(total)
print(add([1,2,3,4,5,6]))    

    