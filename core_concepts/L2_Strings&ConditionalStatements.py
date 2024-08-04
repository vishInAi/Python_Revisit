# Welcome 
print("Welcome to this quick Python Revisit part 2 : Strings and Conditional Statements")

# basic String printing operation
str_eg = "example for printing string"
print(f"\n String Example : {str_eg} now a little more normal")

# Strings Concatenation
str1 = "Hello "
str2 = "boi "
str3 = "Watch and Learn"
# now adding the strings together thats concatenation
concat_str = str1 + str2 + str3
# join can also be used for that 
concat_str1 = " ".join([str1,str2,str3])
print(f"\n String Concatenated using + : \n {str1} + {str2} + {str3} = {concat_str}")
print(f"\n String Concatenated using join : \n { " ".join([str1,str2,str3]) } = {concat_str1}")
# dont mind the extra spaces the join adds them auto and can be useful as well

# Length of String
print(f"\n Length of string '{str_eg}' : {len(str_eg)}")

# Indexing and Slicing of Strings
print("\n Indexing")
print(f" The original string looks like : {str_eg}")
# this shall display the character present at place 2 works like array indexes starts from 0
print(f" certain character at certain place within a string : {str_eg[2]}")

print("\n Slicing")
# we may want to print characters within a range so use ' : ' its Slicing
print(f" Characters printing within a range : {str_eg[0:7]}")
# first index not entered so prints from 0 till inputted index
print(f" Characters printing within a range : {str_eg[:7]}")
# end index not there so just prints all
print(f" Characters printing within a range : {str_eg[0:]}")

# Negative Indexing
n_index_eg = "Banana 🍌"
print("\n Negative Indexing fr")
# putting in negative indexes is possible too
print(f"n_index_eg[-3:-1]: {n_index_eg[-3:-1]}")
print(f"just for fun - n_index_eg[-1] : {n_index_eg[-1]}")
# as you know python can print unix and ascii characters to

# String Functions Cover Up now
str_func = "ai Ml engineer"
print(f"\n Test String : {str_func}")
print("\n String Functions Cover Up :")
# endswith func checks if it ends with certain char or not returns true of false
print(f"Does the string end with '🍌' lets see : {str_func.endswith('🍌')}")
# count func counts a word and its occurence in the string
print(f"Count function of string lets see 'Ai' : {str_func.count('ai')}")

# day 2 was hectic its 10 pm right now so ill just take rest now ....
# will add conditional st and remaining string functions and string related on day 3
# day 3 now 

# capitalize first character
print(f"capitalize first character : {str_func} : {str_func.capitalize()}")

# finds first index of a particular word within a string to show if it exists
print(f"first index of 'engineer' in '{str_func} : {str_func.find('engineer')}'")

# now to replace a part within a string 
print(f"lets replace 'engineer' with 'coder' : {str_func.replace('engineer','coder')}")

# simple practicing of strings

# Program to write first name and second name by input and print it
first_name = input("enter first name : ")
second_name = input("enter second name : ")
print(f"Here we shall print the full name : {first_name+" "+second_name}")
full_name = first_name + second_name
print(f"Length of the full name : {len(full_name)}")

# Program to find the counts and occurences of 🍌 within the string
str_banana = " In the jungle, monkeys swing from 🍌tree to 🍌tree, their favorite snack always being a ripe banana. "
print(f"\n The sentence were testing on : {str_banana}")
print(f"\n Heres the count : {str_banana.count("🍌")} and occurence index : {str_banana.find("🍌")} ")

# Conditional Statements

print("\n Conditional Statements : ")

# Program to grade students based on Marks
marks = float(input(" Enter the Marks you got in the exam : "))
if marks >= 90 :
    grade = "you got an A"
elif marks >= 80:
    grade = "you got a B"
elif marks >= 70:
    grade = "you got an C"
elif marks >= 60:
    grade = "you got an D"
else :
    grade = "you failed lol F"
print(f"Grade : {grade}")

# other exercises in the specific dedicated exercise folder made seperately to do exercises
# core concept Exercises folder 
# Lecture 2 complete


















