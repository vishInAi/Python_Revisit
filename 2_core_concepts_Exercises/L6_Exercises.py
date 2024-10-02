# WAF to print the length of a list (list is the parameter)

list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ]

def numbers(list):
    for i in range(len(list)):
        print(list[i])
    print(f"The length of this list is : {len(list)}")
    return 0
print(numbers(list))

# WAF to print the elements of a list in a single line. ( list is the parameter )

words = ['a','b','c','d']

def symbols(words):
    for i in range(len(words)):
        print(f"{words[i]}", end=' ')    
    return 0
print(symbols(words))

# WAP to print factorial of a number ( make a fuction to do the factorial calculation and return result )

n = int(input("input the number : "))
fact = 1
def cal_fact(n,fact):
    for i in range(1, n+1):
        fact *= i
    print(f"The factorial of the number is : {fact}")
    return 0
cal_fact(n,fact)

#WAF to convert usd to inr

amount = float(input("Enter the Amount : "))
def convert(amount, currency):
    currency = input("usd or inr : ")
    if currency == 'usd':
        yOrno = input("convert to inr? y/n : ")
        if yOrno == 'y':
            print(amount/84)
        else:
            print(f"Here's your USDs : {amount}")
    elif currency == 'inr':
        yOrno = input("convert to usd? y/n : ")
        if yOrno == 'y':
            print(amount*84)
        else:
            print(f"Here's your INRs : {amount}")

convert(amount, '')