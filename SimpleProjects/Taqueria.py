d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def check(d):
    total = 0
    try:
        while True:
            item = input("Item: ").strip()
            normalized_item = item.title()
            if normalized_item in d:
                total += d[normalized_item]
                print(f"${total:.2f}")
            else:
                print("Item not found. Please try again.")
    except EOFError:
        print("\nEOF encountered. Final total: $", total)
    except Exception as e:
        print("An error occurred: ", e)

check(d)