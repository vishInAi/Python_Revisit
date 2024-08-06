# Day 4 : List and tuples

marks = [94.4, 66.4, 95.3, 65.1]
print(f"the marks here are {marks} and their datatype is {type(marks)} and the length of it is {len(marks)}")

# we can store in multiples datatypes in list
student = ['Perry', 23.4, "NY"]
print(f" The data of a student : {student}")
# print by index ( see it works like array indexes is pretty much there )
print(f" The name of the student : {student[0]}")
# if you want to experiment you can try print(student[5]) or any index that doesnt exist in there for knowledge

# List Slicing 🔪
experimental_num = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ]
# initially was gonna use strings and a sentence but putting up quotes made me put numbers 🤣
print(f" ok let's slice but lets take a look at the list : {experimental_num} and its length : {len(experimental_num)} and its type : {type(experimental_num)}")
# lets slice it in 4 diff ways like we sliced the strings in previous lectures
print(f" Numbers upto 4 : {experimental_num[:3]}")
print(f" Numbers in between like 3 to 6 : {experimental_num[2:5]}")
print(f" list starting in middle and ending at the end only : {experimental_num[3:]}")
# now negative index slicing 
print(f" works in reverse gear : {experimental_num[-5:-2]}")
# negative indexes count from right hand side and dont have 0 as first index its just for positives

# LIST METHODS
print("\n List Methods :")
exp_list = [2, 1, 3]
exp_str_list = ['See','it','works','right']
print(f"\n The original list we are working on : {exp_list}")
print(f" The original String list we are working on : {exp_str_list}")
# appending list var.append(index)
print(f" The appended list by using 4 index : {exp_list.append(4)}")
# adds one element at the end of the list
# appended list 
print(f" The appended list : {exp_list}")
# List Sorting
#Ascending var.sort()
print(f" lets see the ascending orded of list : {exp_list.sort()}{exp_list}")
# you can do like exp_list.sorted() too but you know what lets stick to original way  
# Descending var.sort(reverse=True) see the bool values true and false have first letter capital ok
print(f" lets see the descending order of the list : {exp_list.sort(reverse=True)}{exp_list}")
# sort works on strings too
print(f" The string list in ascending : {exp_str_list.sort()}{exp_str_list}")
print(f" The string list in Descending : {exp_str_list.sort(reverse=True)}{exp_str_list}")
# so what happens is the sorting takes up the first characters of each element of string for comparison alphabetically you know right 
# List Insert simply adding element at an index
print(f" Lets add brody within the string list were using : {exp_str_list.insert(2,'Brody')}{exp_str_list}")
# List Remove to remove an element from the list if you want
print(f" Lets make it grammtically better not perfect : {exp_str_list.remove('it')}{exp_str_list} now lets reinstate so i can show you pop method : {exp_str_list.insert(3,"it")}{exp_str_list}")
# list.remove isnt that smart removes the element by taking elemental input but useful
# list.pop removes index saves the type effort lol
print(f" Lets remove it again using the pop : {exp_str_list.pop(3)}{exp_str_list}")

# there are just too many methods but lets rest at this much 

# Tuples now
# just like Lists but they are immutable once declared just cant be modified
print("\n TUPLES NOW")
tup_num = (1,2,3,4,5,6,7,8,9,10) 
tup_str = ('a','b','c','d','e')
# if you want to create a tuple with one element add one comma i know that looks broken but it is what it is eg: tup_str = ( 'w',) like that
# for experimentation two tuples DIFF BW List and Tuples is [] and ()
print(type(tup_num))
print(f" Original tuples we shall use for experimentation : {tup_num} and {tup_str}")
# important methods in tuples :
print(f" count shows count of elements in tuple how many times they exist : {tup_str.count('b')} we expect 1 cause the b exist only once in that tuple")
print (f" Index shows the index of element we put in : {tup_str.index('c')} it'll return 2")
# Tupple Slicing 💀 
print(f" Numbers upto 4 : {tup_num[:3]}")
print(f" Numbers in between like 3 to 6 : {tup_num[2:5]}")
print(f" tuple starting in middle and ending at the end only : {tup_num[3:]}")
# now negative index slicing 
print(f" works in reverse gear : {tup_num[-5:-2]}")
# negative indexes count from right hand side and dont have 0 as first index its just for positives


# and thats it list and tuples covered 















