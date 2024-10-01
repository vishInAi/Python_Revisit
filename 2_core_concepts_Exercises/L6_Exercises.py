# WAF to print the length of a list. ( list is the parameter )

list = ["hi","hello","hey"]
def greet(list):
    for i in range(3):
        print(list[i])

greet(list)

# WAF print the elements of a list in a single line. ( line is the parameter )

num = [1,2,3,4,5,6,7,8]
def numbers(num):
    for i in range(len(num)):
        print(num[i])

numbers(num)        