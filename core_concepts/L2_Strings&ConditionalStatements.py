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
str_func = "Ai Ml engineer"
print(f"\n Test String : {str_func}")
print("\n String Functions Cover Up :")
# endswith func checks if it ends with certain char or not returns true of false
print(f"Does the string end with '🍌' lets see : {str_func.endswith('🍌')}")
# count func counts a word and its occurence in the string
print(f"Count function of string lets see 'Ai' : {str_func.count('Ai')}")

# day 2 was hectic its 10 pm right now so ill just take rest now ....
# will add conditional st and remaining string functions and string related on day 3
# day 3 now 













