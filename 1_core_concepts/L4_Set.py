# Know some concepts such as Union, Intersection, Adding/Removing item, Subset Check, list to set

# Know some concepts such as Union, Intersection, Adding/Removing item, Subset Check, list to set

# Defining a set
set_example = {"element1", "element2", "element3"}
print("Defined set:", set_example)

# Converting a list to a set
list_example = ["element1", "element2", "element1"]
set_example = set(list_example)
print("Converted list to set:", set_example)

# Adding an item to a set
set_example.add("NSYNC")
print("After adding an item:", set_example)

# Removing an item from a set
set_example.remove("NSYNC")
print("After removing an item:", set_example)

# Checking if an item is in a set
is_in_set = "AC/DC" in set_example
print("Is 'AC/DC' in the set?", is_in_set)

# Defining sets
album_set_1 = {"AC/DC", "Back in Black", "The Beatles"}
album_set_2 = {"Back in Black", "Metallica", "AC/DC"}
print("Album Set 1:", album_set_1)
print("Album Set 2:", album_set_2)

# Intersection of two sets
album_set_3 = album_set_1 & album_set_2
print("Intersection of Album Set 1 and 2:", album_set_3)

# Union of two sets
album_set_3 = album_set_1 | album_set_2
print("Union of Album Set 1 and 2:", album_set_3)

# Checking if a set is a subset
is_subset = album_set_3.issubset(album_set_1)
print("Is Album Set 3 a subset of Album Set 1?", is_subset)
