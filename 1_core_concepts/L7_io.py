# file input output operations :

# some rules to remember youknow :
# whenever you open a file be sure to close it as well var_.close()
# read is a default operation if not explicity mentioned.
# text is an default when operating on a file.
# if we read one file completely and perform more op like printing a few char or line itll display blank so close file after each op and open too.

# operations: 
# r - read
# w - write, truncate file
# x - create new, open for writing
# a - open file for writing, appending to end of file if exists
# b - binary mode opens all the files - mp3, png, etc anything that has nothing to do with text.
# t - text mode default.
# + - opens a disk for updating (reading and writing)

# 'r' Read Operation :

f = open("temp.txt", "r") # opening a file and in a certain operation.

text = f.read() # reads entire file
print(text)
f.close()

f = open("temp.txt", "r")
text = f.read(5) # reads no. of char mentioned
print(text)
f.close()

f = open("temp.txt", "r")
text = f.readline() # reads first line
print(text)
f.close()

f = open("temp.txt", "r")
text = f.readlines() # reads multiple lines as per argument
print(text)
f.close()

print(type(text))

# 'w' Write operation :

w = open("tempw.txt", "w")

w.write("Writing something to an empty file hehe")
w.close()

# 'a' Append Operation :

a = open("tempw.txt", "a")

a.write("\nSomething by append function")
a.close()

# 'w+' same as above with truncate :

wr = open ("temp.txt", "w+")

wr.write("(w+ got here overwrite completely)")
wr.close()

# 'r+' overwrite over existing at start lol :

rw = open("temp.txt", "r+")

rw.write("(abc")
rw.close()

# 'a+' same as a+ just at the end of the text file :

ar = open ("temp.txt", "a+")

ar.write("\na+ got here bro here")
ar.close

# io with syntax (it closes file auto) chill papi 💀

with open("temp.txt", "r") as sy:
    data = sy.read()
    print(f"Here's the data : {data}")

with open("temp.txt", "w") as wrsy:
    data1 = wrsy.write("some new shit")
    print(f"here's the data after write : {data1}")

# importing a module

import os
# importing here is not a good practice im just doing it for example's sake

os.remove("some.txt")