def minHouses(r, unit, arr, n):
    if arr is None or n == 0:
        return -1
    totalfoodreq = r * unit
    foodtillnow = 0
    
    for house in range(n):
        foodtillnow += arr[house]
        if foodtillnow >= totalfoodreq:
            return house + 1
    
    return 0

r = int(input("The number of rats: "))
unit = int(input("Amount of food each rat requires: "))
n = int(input("Number of houses: "))

arr = []  # Initialize an empty list to store the food amounts
for i in range(n):
    food_amount = int(input(f"Food amount at house {i + 1}: "))
    arr.append(food_amount)

print(minHouses(r, unit, arr, n))
