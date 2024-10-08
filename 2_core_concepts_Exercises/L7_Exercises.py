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