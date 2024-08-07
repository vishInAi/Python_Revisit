# Day 5 : Dictionary and Sets in python

# Dictionary : just like the lists but store key : value pairs as one element
# mutable unordered and dont allow duplicate keys

dict = {
    "name" : "Vishwesh", # string key string value
    "cgpa" : 9.6, # string key float value
    "marks" : [98,97,96], # string key and a fkin list lol 
}
# Dictionaries are pretty flexible
# above one we can use too but for now lets just keep it as example and use the below for experimentation

info = {
    "key" : "value",
    "name" : "Some_student",
    "course" : "Ai",
    "age" : 21,
    "is_adult" : True,
    "marks" : 97.7,
    "tup" : ("see",'even',"tuples",'work')

}
print(f"\n the dictionary we are going to work on : {info}")
# key prints the specific value in dict
print(f"\n {info["course"]}")
# Indexes works too
info["name"] = "Brody" # overwrites
info["sirname"] = "Biden" 

print(f"\n Full name : {info["name"]} {info["sirname"]} ")
# see Nested dictionary now :
brody_subjects = {
    "name" : "Trump",
    "subjects" : {
    "chem" : 98,
    "math" : 95,
    "phy" : 97,    
    }
}
print(brody_subjects["name"], brody_subjects["subjects"]["chem"])

# Typecasting fr 
print(list(brody_subjects.keys()))
# can use methods too like function in function in function in function .....
print(len(list(brody_subjects["subjects"])))

# key return in dictionary 
print(f"\n Keys return : {brody_subjects.keys()}")
# Return all values
print(f"\n values return : {brody_subjects.values()}")
# return all key value as pairs as tuples
print(f"\n items return : {brody_subjects.items()}")
# returns Returns value according to key get will not give errors in case of wrong key which normal syntax would do
print(f"\n Keys return : {brody_subjects.get("name")}")
# update adds items into dictionary from other dictionary
print(f"\n Keys return : {brody_subjects.update(dict)} {brody_subjects}")

# Sets in Python
# like in maths : unordered items collection
# each element in set be unique and immutable

print("\n SETS IN PYTHON : ")
# set acceptable datatypes : bool int float str tuple

nums = {1,2,3,4,"hello","there"}
print(type(nums))
print(nums)
print(len(nums))

# empty set 
empty = set()
print(type(empty))

# note : set elements are immutable not the set itself

# Set Methods : 
print("\n Set Methods : ")

# 1 add element method
# lets add elements into that empty set 
empty.add(1)
empty.add(2)
empty.add(3)
# sets dont like duplicate elements so just see
empty.add(3)

print(type(empty))
print(empty)
print(len(empty))

# 2 remove element method

empty.remove(2)
# removes the 2 from that set
print(empty)

# 3 clear method
empty.clear()
# remove all elements 
print(empty)

# lets add some elements to experiment further

empty.add(1)
empty.add(2)
empty.add(3)
empty.add(4)
empty.add(5)
empty.add(6)
empty.add(7)

print(len(empty))
print(empty)

# 4 pop method
# pop gives out random value

print(empty.pop())
print(empty.pop())
print(empty.pop())

# just pops random values 

# 5 union method
# combines both set values and returns new set out of them
print(empty.union(nums))
# it doesnt repeat so it wont here either

# intersection : like maths see whats common in both and print it
print(empty.intersection(nums))
# pop is set up already thatll remove a few elements before check so beware lol youd think something is wrong 🍌 but nothing is
# doesnt repeat you see

# Thats Day 5 Dictionary and sets for ya
# contribute if possible









