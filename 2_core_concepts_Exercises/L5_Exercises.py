# While Loop Exercises

# Program 1 : print numbers 1 to 100
i = 1
while i <= 100:
    print(i)
    i+=1

# Program 2 : print numbers 100 to 1
while i>=1 : 
    print(i)
    i-=1

# Program 3 : Print Multiplication Table of a number n

num = int(input("input a number you want table of : "))
j = 1
while j<=10:
    print(num*j)
    j+=1


# Program 4 : Print x numbers in this tuple using loop (question doesnt make sense ikr anyway)
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

num_tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
k = 0
print(f" All the Numbers till x :")
while k<=9 :
    print(num_tup[k])
    k+=1


