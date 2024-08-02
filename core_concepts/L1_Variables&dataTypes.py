# welcome_message
print("Welcome to this Quick Revisit into Python")

# var assignment of diff data types
name="Vishwesh"
age=20
price=60000000000.00
# Apollo Hospitals states that the notional value of a single human body could be as high as $6,000,000,000 😂

print("\n Variables declared above and their values : ")
# dont mind the F in below print statements its just a string literal
print(f" Name : {name}")
print(f" Age : {age}")
print(f" Price : {price}")

# Python Characterset
letters ="A to Z & a to z"
digits ="0 to 9"
special_symbols ="+,-,/,*,etc."
whitespaces ="Blank Space, tab, carriage return, newline, formfeed"
# Ascii and unicode are compatible too

print(f"\n Python Charactersets : ")
print(f" Letters : {letters}")
print(f" Digits : {digits}")
print(f" Special Symbols : {special_symbols}")
print(f" Whitespaces : {whitespaces}")
print(f" Ascii and unicode are also compatible : 😂")

# Data types
print("\n DataTypes in Python : ")
print(f"Integer : {age} (type : {type(age)})")
print(f"String : {name} (type : {type(name)})")
print(f"Float : {price} (type : {type(price)})")
bool_eg = True
print(f"Boolean : {bool_eg} (type : {type(bool_eg)})")

# Keywords
keywords_eg = "False"
print(f"\n Keywords in Python (e.g., False) should always be upper case : {keywords_eg} ")

# Comments in python
print("\n Comments in Python : ")
print(" '#' starts a single line comment in python ")
print(' """comment"""  now this can produce multiline comment triple double quotes')

"""
multiline 
Comment 
Right 
Here
"""

# Arithmetic Operations
# lets use alphabets for vars pretty easy to use then
a = 5
b = 3
print ("\n Arithmetic Operations : ")
print (f"Addition : {a+b}")
print (f"Substraction : {a-b}")
print (f"Multiplication : {a*b}")
print (f"Division : {a/b}")
print (f"Modulus : {a%b}")
print (f"Exponentiation : {a**b}")

# I can add Input prompts too but just going with whatever the lecture 1 is teaching

# Relational / Comparison Operators
# a value is set at 5 and b value is set at 3 
print("\n Relational / Comparison Operators : ")
print(f" Syntax : a == b in performance : { a == b }")
print(f" Syntax : a != b in performance : { a != b }")
print(f" Syntax : a < b in performance : { a < b }")
print(f" Syntax : a > b in performance : { a >= b }")
print(f" Syntax : a <= b in performance : { a <= b }")
print(f" Syntax : a >= b in performance : { a >= b }")

# Ok lets exploit one variable by testing all Assignment operators on it 🥽
print("\n Assignment Operators : ")
assign = 10
assign += 2
print(f" assign+=2 : {assign}")
assign -= 2
print(f" assign-=2 : {assign}")
assign *= 2
print(f" assign*=2 : {assign}")
assign /= 2
print(f" assign/=2 : {assign}")
assign %= 2
print(f" assign%=2 : {assign}")
assign **= 2
print(f" assign**=2 : {assign}")

# Logical Operators
print("\n Logical Operators : ")
x = True
y = False
print(f" not operator : { not x}")
print(f" and operator : {x and y}")
print(f" or operator : {x or y}")

# Type Conversion
print("\n Type Conversion : ")
a,b = 1,2.0
sum = a+b
print(f"sum of integer and float (1+2.0) : {sum} (type : {type(sum)})")

# Type Casting
a,b = 1,"2"
# as you can see its one int and another string as i declared a and b above
c = int(b)
# we stopped c from taking string value forced b's value to be taken up as integer
sum1 = a+c 
print(f"Type casting string to int and adding so like a+int(b)+c : {a+int(b)+c} output will be 5")

# input in python
print("\n Input in Python : ")
user_int = int(input("Enter an Integer (cause you can) : "))
user_float = int(input("Enter an float (remember to add decimal points or itll add auto) : "))
user_string = input("Enter a String : ")
# ok one output to show the inputs working
print(f"the integer entered : {user_int} , the float entered : {user_float} , the string entered : {user_string}")

# they gave some exercises in that lecture so ill setup another folder within the repository to do them.





