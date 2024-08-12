# Loops in Python

# While Loop
count = 1

while count <= 5 :
    print("Hello world")
    count+=1

print(count)

# Block & Continue

count = 1
while count<=5 :
    print("Hello World")
    if count == 3 :
        print("count reached 3")
        break
    count += 1

count = 0
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
num_search = int(input("Enter the Number you want to search : "))
while count < len(nums) :
    print ("Looking for it ...")
    if nums[count] == num_search :
        print ("\n Found the number 🍌")
        print (f"\n The number you were looking for {nums[count]} is at index {count} ")
        break
    count += 1
else :
    print ("\n Number not found 🥕") 
# use break wisely its not a switch statement its just for some exceptions if you wanna use it

# lets use continue now

count = 0
while count <= 10 :
    if count%3 == 0 :
        count +=1
        continue
    print (f" numbers : {count}")
    count +=1
# its simply used to keep the loop going by skipping certain stuff you wanna skip

# lets see for loop now
count = 0
veggies = ["potatoes","brinjal","cucumber","ladysfinger"]
for char in veggies:
    print (veggies[count])
    count+=1
str_veggie = "potatoes"
for char in str_veggie:
    print(char)
    if char == "o":
        print("found o")
        break
else:
    print("End")

# Range stuff in Loops

for el in range(5): # range(stop)
    print(el)
for el in range(1,5): # range(start, stop)
    print(el)
for el in range(1,5,2): # range(start, stop, step)
    print(el)
# its late night ill update it whenever i get time or atleast put up a better example for the range 
# range(start?,stop,step?)



