# Exception Classes today 💀

#  print("Hello World)  try running this you get 
# Exception.py", line 3
#   print("Hello World)
#         ^
# SyntaxError: unterminated string literal (detected at line 3)

# x = int(input("What's x? "))
# print(f"x is {x}")

# if i input anything other than int it'll throw
# Exception.py", line 11, in <module>        
#   x = int(input("What's x? "))
#       ^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'cat'

# how to deal ? see below now :

# simple : returns output and stop

try:
    x = int(input("what's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")

# now name error :

# print(f"x is {x}") 

# cause x is an int and it cant output whatever you enter

# Exception.py", line 30, in <module>        
#    print(f"x is {x}")
#                  ^
# NameError: name 'x' is not defined
while True:
    
    try:
        y = (int(input("What's y?")))
    except ValueError:
        print("y is not an integer")
    else:
        print(f"y is {y}")
        if isinstance(y, int):
            break
    

print(f"y is {y}")

# creating functions with try except

def main():
    z = get_int()
    print(f"z is {z}")

def get_int():
    while True:
        try:
            z = int(input("Input value of Z : "))
        except ValueError:
            print("Z is not an integer") # you can also remove else and the return all together and itll work the same
        else:
            break # you can return z in else as well and it can break loop as well
    return z

main()

# tf is pass

def main1():
    a = get_int1("Input:") # cause we put prompt below in getint and a = getint a will acquire the value of prompt arg
    print(f"a is {a}")

def get_int1(prompt): # we can use an argument and put the return in the try to stop the loop
    while True:
        try:
            return int(input(f"Input value of A : {prompt} "))
        except ValueError:
            print("A is not an integer") # you can also remove else and the return all together and itll work the same
            pass

main1()

