# String Methods:

# 1. Title Method : 

print("Haggu is king of the World".title())

# 2. Split Method :

temp = "daylight: 260 F Nighttime: -280 F"
temp_list = temp.split() # sep word by word
print(temp_list)

temp = "daylight: 260 F . Nighttime: -280 F"
temp_list = temp.split(".") # split by anything within string
print(temp_list)

# 3. Find Method :

print("moon" in "moon isnt white.")
# method is case sensitive too ok whatever search keep it as it should be in string
print("moon" in "nat_satellite is just reflecting.")

temp = "it is what it is"
print(temp.find("what")) # case sensitive will output : the pos of start of whatever searched
print(temp.find("moon")) # returns -1 cause it wasnt able to find

# 4. count method :

temp = "slim shady is slim shady"
print(temp.count("slim")) # return 2 if found and the count
print(temp.count("snoop")) # doesnt exist no count return 0

# 5. Lower & Upper method :

temp = "AMERICA IS great for opportunities." # you can join the lower here as well depends what you wanna do
print(temp.lower())

temp = "Capt. America is 2nd best".upper()
print(temp) # can join the upper() here too just like the lower in above example

# 6. Checking content using slicing

temp = "it is what it is"
part = temp.split()
print(part)
print(part[-1]) # prints the last element

# 7. isnemeric Method

temp = "yesterday the temps were reaching 50 C"
for item in temp.split():
    if item.isnumeric(): # finds numeric in the item list
        print(item)

temp = "the new burger costs 5.50 $"
for item in temp.split():
    if item.isdecimal(): # finds decimal in the item list
        print(item) 

# Transform Text

print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C"))
# This will replace certain part of string by identified by it with whatever arg given to it 

temp = "Temp on the moon can vary wildly"
print("temp" in temp) # returns false cause of case sensitivity
temp = temp.lower() 
print("temp" in temp ) # returns true cause we transformed the text earlier
print("temp" in temp.lower()) # if you dont wanna store temp val again you can do this as well

# Join Method
 
temp = temp.split()
# we just converted temp into a list ok

print(temp) # returns with sq brackets in list format
print(' '.join(temp)) # returns in string format and uses the ' ' space to join all the items in it

