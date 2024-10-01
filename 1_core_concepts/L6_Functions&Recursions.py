# function declaration

a= 0
b= 0


a = int(input("Input any two digit number : "))
b = int(input("Input any two digit number : "))

def cal_sum(a,b):
    s = a+b
    return s

print(f"the sum of two numbers is : {cal_sum(a,b)}")

# as you can see we input two digits above and printed their output too but now we will use the function for more sums

print(cal_sum(75,56))

# now inputing different digits and their sum

print(cal_sum(343,563))

# this decreases redundancy of code and the no of lines

# now how do we store the values in another vars for later use

add = print(cal_sum(int(input("\nInput the dynamic number : ")),int(input("\nInput the 2nd dynamic number in the sum : "))))

def print_hello():
    print("hello")
    
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

hey = print_hello()

print("\n")
print(hey)



