# i = 1 
# while i<=100:
#     print(i)
#     i+=1


# i = 100
# while i >=1:
#     print(i)
#     i-=1    


# n = 2
# i = 1
# while  i <=10:
#     print(i*n)
#     i+=1   

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# j =0
# while j <= 9:
#     print(nums[j])
#     j+=1


# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 16
# j = 0
# while j <= 9:
#     if(nums[j]==x):
#        print("at index",j)
#     j+=1


# i = 1
# while i <= 20:
#     print(i)
#     i += 1
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit
#     temp // 10    
# print(f"Sum of digits of {num} is {sum}")

# while True:
#    user = input("enter name ")
#    if user == "exit":
#        print("loop end")
#        break
   
# num = int(input("Enter a number: "))
# a ,b = 0 ,1
# count = 1
# while count <= num :
#     print(a ,end=" ")
#     next = a+b
#     a = b
#     b = next
#     count += 1
import random
secret = random.randint(1 , 10)

while True:
    num = int(input("Enter a number: "))

    if secret == num:
        print ("correct")
        break
    if num < secret :
        print("to low")
    if num > secret :
        print("to high")    
