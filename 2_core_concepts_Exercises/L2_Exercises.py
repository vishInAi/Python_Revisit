# Lesson 2 : Exercises

# WAP Program to check if a number entered by the user is odd or even
print("\n Even or Odd Checker : \n")
number = int(input("Enter a number to check if its odd or not : "))
if number % 2 == 0: 
    print(f"The inputted number {number} is EVEN 🌟")
else :
    print(f"The inputted number {number} is ODD 🍌")

# WAP to find the greatest among 3 numbers entered by the user
print("\n Greatest number finder : \n")
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
num3 = float(input("Enter the third number : "))
# ok just taking in 3 different numbers from the user 
# conditional statements will play role in comparing the inputs and giving out the greatest of above 3
# we can do great things by like making an array inputting lots of numbers and comparing them all but for now lets stick to simpler exercise as its core concepts stuff
if num1 > num2 and num1 > num3:
    print(f"The first number {num1} is greatest among all 3")
elif num2 > num1 and num2 > num3:
    print(f"The Second number {num2} is greatest among all 3")
else : 
    print(f"Third number is greatest {num3}")

# 2nd version of same code two save some text and effort i guess
if num1 > num2 and num1 > num3:
    greatest=num1
elif num2 > num1 and num2 > num3:
    greatest=num2
else : 
    greatest=num3

print(f"The greatest of {num1} ,{num2}, {num3} is {greatest}")
# typing effort saved

# WAP to check if a number is a multiple of a 'certain number' or not
print("\n Multiple or not Multiple : \n")
certain_number = int(input("Input the number you'd like to find multiples of : "))
num = int(input("Input a number you want to check if its a multiple of above entered certain number 😅 : "))
if num % certain_number == 0 :
    print(f"Yup the number you put in '{num}' is a multiple of '{certain_number}'")
else:
    print(f"{num} is not multiple of {certain_number}")

"""  
fork the repo and see if you can add a few more exercises 
without dependencies or errors use branches to send in PRs
like a new branch named exercise that'd be cool.
"""

    




