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

# 'r+' append at start lol :

rw = open("temp.txt", "r+")

rw.write("it'")
rw.close()