# create a new file practice.txt using py then add :
# hi everyone
# we are learning file i/o
# using java
# i like programming in java

with open("practice.txt", "w") as f:
    data = f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
    print(data)

# New function to learn replace ("existingtext", "newtext")

with open("practice.txt", "r") as r:
    data1 = r.read()

update = data1.replace("Java", "Python")
print(update)

with open ("practice.txt", "w") as f:
    f.write(update)

# search if the word learning exists in the file or not
word = str(input("tell what to search : "))
with open("temp.txt", "r") as find:
    data = find.read()
    if (data.find(word) != 1):
        print("found")
    else:
        print("not found 🍌")

# WAF to find in whick of the file does the word "learning" occur first print -1 if word not found.

def check():
    words = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
            line_no += 1
    return -1

print(check())

# from a file containing numbers seperated by commas, print the count of even numbers.
count = 0
with open("practice1.txt", "r") as even:
    data = even.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)