# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

# number = input("enter a age: ")
# number = int(number) 
# if number > 18:
#     print("You are an adult")
# elif number < 18: 
#     print("you are a minor")
# elif number == 18:
#     print("you are 18 years old")

# my_string = ""

# if my_string:
#     print("The string is not empty")
# else:
#     print("The string is empty")

# print(bool("")) # false 
# print(bool(None)) # false
# print(bool(0)) # false 
# print(bool(False)) # false 
# print(bool(0.0)) # false 

# if not my_string:
#     print("The string is empty") 

# age = int(input("Enter your age: "))
# print("You are an adult") if age >= 18 else print("You are a minor")



# name = "Тарас"
# age = 25
# has_driver_licence = True

# if name == "Тарас": 
#     print("you are Тарас")
# else:
#     print("you are not Тарас")
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are a minor")
# if has_driver_licence:
#     print("You have a driver's licence")
# else:
#     print("You do not have a driver's licence")

# if age >= 18 or has_driver_licence:
#     print(f"{name} you are welcome to drive")



# x = int(input("Enter a numberx "))
# y = int(input("Enter a numbery "))
# z = int(input("Enter a numberz "))

# if x > y and x > z:
#     print(f"{x} is the largest number") 
# if y > x and y > z:
#     print(f"{y} is the largest number")
# if z > x and z > y: 
#     print(f"{z} is the largest number")



# water_temperature = int(input("Enter water temperature: "))

# if water_temperature < 0:
#     print("Water is frozen")
# if water_temperature >= 0 and water_temperature < 100:
#     print("Water is liquid")
# if water_temperature >= 100:
#     print("Water is gas") 


# my_string = "Hello, World!"
# for char in my_string:
#     # print(f"Character: {char}")
#     print(char, end="?")


# my_string = "what a wonderful day"
# count = 0

# for char in my_string:
#     if char == "a":
#         count += 1

# print(f"The letter 'a' appears {count} times in the string.")


# my_string = "what a wonderful day"
# count = 0

# for char in my_string:
#     count += 1 

# print(f"The string has {count} characters.")


# my_string = "what a wonderful day"
# for i, char in enumerate(my_string, start=1):
#     print(f"character symbol {char} has index {i}")
#     pass

# print(f"Number of characters: {i} - {char}")


# for i in range(1, 11, 2):
#     print(i)


# for i in range(1, 11,):
#     if i == 5:
#         print("cycle has not ended yet")
#         break
# else:
#     print("Cycle has ended")

# print(f"{i =}")


# for  i in range(20): 
#     if i % 3 == 0:
#         print(f"{i} can be divided by 3 without a remainder")
#         continue 

#     print(f"{i} is an odd number")
# else:
#     print("is there anything after continue?")


# my_string = "Hello"

# for i in range(15):
#     print(f"{my_string} - {i}")



# a = input("Enter the first number: ")
# b = input("Enter the second number: ")

# if a.isdigit() and b.isdigit():
#     a = int(a)
#     b = int(b)

#     for i in range(a, b+1):
#         if i % 2 == 0:
#             print(i)
# else:
#         print("u haven't entered a number")



# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# #print header
# print(end = '\t')
# for i in range(c, d + 1) :
#     print(i, end = '\t')
# print("")

# #print table
# for i in range(a, b + 1) :
#     print(i, end = '\t')
#     for j in range(c, d + 1) :
#         print(i * j, end = '\t')
#     print("")



# a = 2
# while a < 6: 
#     a+= 1 
#     print(f"{a = }")

# mystring_1 = "hello"
# mystring_2 = "world"
# # print(len(mystring_1))
# i = 0
# while len(mystring_1) < 40:
#     mystring_1 += mystring_2 
#     i += 1 

# print(f"{mystring_1 = }")
# print(f"{len(mystring_1) = }")


# while True: 
#     my_string = input("enter ur question or enter exit to exit:")
#     if my_string.lower() == "exit":
#         print("exiting the program...")
#         break
#     print(f"your question is {my_string}")

# print("program has ended")

# numbers = [i for i in range(20)]
# print(numbers)


# sum = 0 
# count = 0 
# for i in range(20):
#     if i % 3 == 0:
#         sum += i
#         count += 1

# avg = sum / count 
# print(f"Average of multiples of 3 in the range 0-19 is: {avg}")



# for i in range(20, 200):
#     if i < 100:
#         print(f"{i} bigger than 20 but less than 100")
#     else:
#         print(f"{i} bigger than 100 but less than 200")



# for i in range(20): 
#     print(f"{i = }")
#     for j in range(20):
#         print(f"{i = }")
#         if j > 3: 
#             break 
#         break 





# n = int(input("Enter a number between 1 and 999: "))

# if 1 <= n <= 999:
#     if n % 2 == 0:
#         print("the number is even")
#     elif n % 3 == 0: 
#         print("the number is not even")
# if 1 <= n <= 999:
#     if 10:
#         print("The number has 1 digit.")
#     elif n < 100:
#         print("The number has 2 digits.")
#     else:
#         print("The number has 3 digits.")
# else:
#     print("Invalid input. Please enter a number between 1 and 999.")



# while True: 
#     number = input("enter a number 1 - 999")
#     if not number.isdigit() or 1 < int(number) < 999: 
#         print("u didnt enter a nuber or the number isnt right")
#         continue 

#     number = int(number)
#     if number < 1 or number > 100: 
#         name = "one digit Number"
#     elif number < 100: 
#         name = "two digit Number"
#     else: 
#         name = "three digit Number"

#     is_odd = True if number % 2 == 0 else False 
#     print(f"Number{"even" if is_odd else "not even"} {name}")



a = int(input("enter first number "))
b = int(input("enter second number "))
multiple = 1

for i in range(a, b + 1):
    multiple *= i

print(f"the answer to {a} multiplied by {b} is {multiple}")

