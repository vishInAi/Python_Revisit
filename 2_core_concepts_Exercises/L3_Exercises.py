print("Exercises of Lesson 3 : ")

# exercise 1 : WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
print("\n 3 Movies that you'd like to remember store them in this list :")
movie_input = []
movie_input = input(),input(),input()
# professionals use append make the code big one more variable declaration needed but see im running a lil late its already 10:30 pm lol
print(f"the list you entered : {movie_input}")

# exercise 2 : WAP to check if a list contains a palindrome of elements. (hint use copy method fr)
print("\n Lets just check the list for a palindrome of elements : ")
list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if copy_list1 == list1 :
    print("palindrome")
else : 
    print("not a palindrome")

# exercise 3 : WAP to count the number of Students with A grade in the following tuple
# (c,d,a,a,b,b,a)

print("\n Grade Counter :")
grades = ('c','d','a','a','b','b','a')
print(f" the grade you wanna check how many students got it (a,b,c,d): ")
grade_to_check = input()
print(f" The {grade_to_check} Grade have been attained by {grades.count(grade_to_check)} Students")
