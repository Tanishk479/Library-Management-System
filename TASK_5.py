#WAP TO PRINT SERIES FROM 3 TO 39
# for i in range(3,40):

#     print(i)
# #WAP TO PRINT SERIES FROM 15 to 5
# for i in range(15,6,-1):
#     print(i)
#WAP TO PRINT number div by 7 (1,21)
# for i in range(1,22,7):
#     print(i)

#WAP TO PRINT count of total numbber of divisor of given number
# n=int(input("enter the number"))
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# print("total number of divisor is",count)
#7.
# n=int(input("enter the number : "))
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print(f'{n} is a prime number')
# else:    
#     print(f'{n} is not a prime number')

#8.
# sum = 0
# for i in range(3,10):
#     sum +=i
# print("the sum of the series is",sum)

#9.
# n = int(input("enter the number : "))
# sum =0
# while n>0:
#     sum += n%10
#     n //= 10
# print("the sum of the digits is",sum)

#or 
# n = int(input("enter the number : "))
# sum = 0
# for i in str(n):
#     sum += int(i)
# print("the sum of the digits is",sum)

#10.
#wap to sum of odd digits present in the given number
n = int(input("enter the number : "))

sum = sum(int(i) for i in str(n) if int(i)%2==1)
print("the sum of the odd digits is",sum)

# for i in str(n):
#      sum += int(i)%2==1 and int(i) or 0
# print("the sum of the odd digits is",sum)

# for i in str(n):
#     if int(i)%2==1:
#         sum += int(i)
# print("the sum of the odd digits is",sum)