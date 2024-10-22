"""
Exercise 1 : Store following word meanings in a python dictionary :

table : “a piece of furniture” , “list of facts & figures”
cat : “a small animal”

"""

words = {
    "table" : ["a piece of furniture","list of facts & figures"],
    "cat" : "a small animal"
         }
# simple py dictionary created and multiple values in one key stored as well
print(f" The simple Python Dictionary : \n {words}" )

"""
Exercise 2 : You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.

”python”,“java”,“C++”,“python",“javascript”,“java",“python”,“java”,“C++”,“C”
"""
# simply use a set cause it takes unique values not duplicates
classrooms = {
    "python", "java", "cpp", "python", "javascript", "java", "python", "java", "cpp", "c"
    }
print(f"printing the total number of classrooms required as per subjects taken by students : {len(classrooms)}")

"""
Exercise 3 : WAP a enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one.
use Subject name as key and Marks as value
"""

Report_card = {}
print("\n Enter the subject name and the associated marks too below : ")
subject = input("\n Enter Subject name : ")
marks = int(input("\n Enter the Subject marks : "))
Report_card[subject] = marks

subject = input("\n Enter Subject name : ")
marks = int(input("\n Enter the Subject marks : "))
Report_card[subject] = marks

subject = input("\n Enter Subject name : ")
marks = int(input("\n Enter the Subject marks : "))
Report_card[subject] = marks

print(Report_card)

"""
Exercise 4 : Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)

"""

Exp_set = {}
Exp_set = int(input()),float(input())
print(f"\n The Values stored seperately in the set : {Exp_set}")