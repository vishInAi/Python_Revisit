# e.g. :  '/resources/data/Example1.txt'
#         ^   directory   ^  fileName  ^

# we may initiate file operations in a way such as :

#  file1 = open('/resources/data/Example1.txt','r')
#  ^name^ Method ^   directory   ^  fileName ^mode^

# But importantly we need to close the file operation as well using close method.
#  file1.close() 

# This can get tedious so we can use a 'with' statement as well

# ' with open("Example1.txt","r")as File1: '  -> Look close File1 is an object ok
# '     file_stuff=File1.read()            '  -> Method read used here
# '     print(file_stuff)                  '  -> printing file stuff
# ' print(File1.closed)                    '  -> Statement to know if file closed sucessfully and not for closing ok just checking
# ' print(file_stuff)                      '  -> file is closed but content is still in the file_stuff var so we can print outside 'with' as well.

# the with statement will let us open file do operations as well and it will close the file auto

# ' with open("Example1.txt","r")as File1: '
# ' file_stuff = File1.readlines()         ' -> Basically turning every line in the file into a list of seperate elements one line = one element in the list
# ' print(file_stuff)                      '

# We can Print each line Individually as well ( Using For Loop ): 

# ' for line in File1:                     '
# '    print(line)                         '

# Representing every character in a string as a grid :

# ' file_stuff = File1.readlines(4)        '
# ' print(file_stuff)                      '

# we can specify the number of characters we would like to read froma string as an argument.

# e.g. : theres a file containing some stuff :
# this line 1
# this line 2
# this line 3

# using like grid wont pass line but rather take as many number of characters it has been told to pick line by line ok
# ' file_stuff = File1.readlines(11)       ' -> >this line 1<
# ' file_stuff = File1.readlines(5)        ' -> >this <
# ' file_stuff = File1.readlines(6)        ' -> >line 2<
# #


# Data attributes 
# name - to check name of file e.g. : file1.name   'used like this to show file name with obj file1'
# mode - to check the mode of file e.g. : file1.mode   'used like this to see the mode of file used with the file instance ok'

# The Modes :
# r - Basic Read Mode, just views as output in console.
# w - Write Mode, add stuff by removing old data completely.
# a - Append, adds stuff at end of file.
