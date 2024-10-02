# test

def show(n):
    if (n==0):
        return # you need base cases like the if and return so that the recursion stops at some point else itll run endlessely and crash
    print(n)
    show(n-5)

show(100)

def fact(f):
    if(f == 0 or f == 1):
        return 1
    else:
        return(f*fact(f-1))

print(fact(4))
