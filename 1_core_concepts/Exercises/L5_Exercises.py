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
print(f"\nAll the Numbers till x :")
while k<=9 :
    print(num_tup[k])
    k+=1

# program 5 : for loop : Print the elements fo the following list using a loop
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

print("\nPrinting Numbers in the List : ")
num_list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for num in num_list:
    print(num)
    num+=1

# program 6 : for loop : searching for number x in the from the tuple 
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

print("\nSearching number from within the Tuple ")
num_find = int(input("\nInput the number you want to find : "))
for i in range(len(num_tup)):
    print("Working on it...")
    if num_tup[i] == num_find:
        print (f"See what we found : {num_tup[i]} at index {i}")
        break
else:
    print("\nWe didnt find the Number 🍌")

# program 7 : for loop : print numbers 1 to 100

for j in range(1,101):
    print(j)

# program 8 : for loop : print numbers 100 to 1

# enough for today



