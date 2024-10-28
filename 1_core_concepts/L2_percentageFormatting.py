# String Percentage Formatting

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage) # look at that %s and the var we called right after the % we are putting value stored in var inplace of that %s ok

# formatting from a set i suppose 

temp = ("Moon", "Earth", "Moon", "Earth")
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % temp)
# upper example or the below one both the same
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))

# format() Method

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage)) # works just like percentage formatting but uses .format(var_name)

# using index to format

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage)) # 0 is moon and 1 is whatever store in the var here

# identifying uniquely with strings in curly braces and replacement

mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

# f strings

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
# curly braces can let you use variables of calculations or anything. content in {} is not treated as strings just know that much haha.
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# adv lvl stuff in f strings not that much but i didnt knew if we can do this too lol 💀
subject = "interesting facts about the moon"
heading = f"{subject.title()}" # the subject string is being stored and tile method is being applied and you are storing a string in another var with f string formatting know that this is some out of the box stuff
print(heading) # printing heading now and one more f is not just used in print function ok