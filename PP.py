


# Construct a Python program that reads numbers from the
# user until they enter 0. The program should skip negative
# numbers using continue, stop taking input if the sum
# exceeds 50 using break, and use pass for numbers that are
# multiples of 5
# num = int(input("enter the number(0 to stop) : "))
# sum = 0
# while num != 0:
#     if num < 0:
#         print("negative number is skipped")
#         num = int(input("enter the number(0 to stop) : "))
#         continue
#     if sum > 50:
#         print("sum exceeded 50, stopping input")
#         break
#     if num % 5 == 0:
#         print("number is a multiple of 5, using pass")
#         num = int(input("enter the number(0 to stop) : "))
#         pass
#     sum += num
# #     print("current sum:", sum)

# total_sum = 0

# while True:
#     num = int(input("Enter a number (0 to stop): "))

#     # Stop if user enters 0
#     if num == 0:
#         break

#     # Skip negative numbers
#     if num < 0:
#         continue

#     # Use pass for multiples of 5
#     if num % 5 == 0:
#         pass  # No special action, just placeholder

#     # Add to sum
#     total_sum += num

#     # Stop if sum exceeds 50
#     if total_sum > 50:
#         print("Sum exceeded 50. Stopping input.")
#         break

# print("Final Sum:", total_sum)

for i in range(1,6):
    for j in range(1,11):
        print(i,"*",j,"=",i*j )
    print(end=" ")
    print()

