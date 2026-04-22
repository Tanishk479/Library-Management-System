# # strong number
# def strong_no_check(n):
#     sum = 0
#     for i in str(n):
#         fact = 1
#         for j in range(1,int(i)+1):
#             fact *= j
#         sum += fact
#     if n==sum:
#         print(f'{n} is a strong number')
#     else:
#         print(f'{n} is not a strong number')
# strong_no_check(int(input("enter the number : ")))


# WE CAN access gloabal variable in many space 
# but we can not access local variable outside the function
#but if we want to access local variable outside the function 
#then we use global keyword
# a = 10
# print(a)
# def fun():
#     global a
#     a = 20
#     print(a)
# fun()
# print(a)


# def outer():
#     a = 10
#     print(a)
#     def inner():
#         a = 20
#         print(a)
#     inner()
#     print(a)
# outer()

#inside type of variable is local variable
#to modify local variable inside nested function we use nonlocal keyword
#outside type of variable is global variable

# #print the pattern of square
# def outer():
#     for i in range(1,6):
#         for j in range(1,6):
#             print("*",end=" ")
#         print()

# def outer():
    
#     a = 10
#     print(a)
#     def inner():
#         nonlocal a  #scope of this variable is inside this function and outer function
#         a = 20
#         print(a)
#     inner()
#     print(a)
# outer()
# print(a)


#function to extarct vowels present inside string ond count of vowels
# def count_vowels(s):
#     dic = {}
#     for ch in s :
#         if ch in "aeiouAEIOU":
#             if ch in dic:
#                 dic[ch] += 1
#             else:
#                 dic[ch] = 1
#     return dic
# print(count_vowels("abcddeee"))

# def count_vowels(s):
#     count = 0
#     for ch in s :
#         if ch in "aeiouAEIOU":
#             if ch in dic:
#                 dic[ch] += 1
#             else:
#                 dic[ch] = 1
#     return dic
# print(count_vowels("abcddeee"))
 #break , continue , pass is only used in loops

# lst = [10, 20, 30, 40, 50]
# tup = (1, 2, 3, 4, 5)

# print(lst[1:4])     # [20, 30, 40]
# print(lst[:3])      # [10, 20, 30]
# print(lst[::2])     # [10, 30, 50]

# print(tup[2:5])     # (3, 4, 5)
# print(tup[::-1])    # (5, 4, 3, 2, 1)
import math
print(math.sqrt(16))