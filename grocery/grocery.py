def main():
    grocery_list = []

    try:
        while True:
            item = input("Item: ").strip().lower()
            grocery_list.append(item)
    except EOFError:
        print_grocery_list(grocery_list)

def print_grocery_list(grocery_list):
    quantities = {}
    for item in grocery_list:
        if item in quantities:
            quantities[item] += 1
        else:
            quantities[item] = 1

    for item in sorted(quantities.keys()):
        print(f"{quantities[item]} {item.upper()}")

if __name__ == "__main__":
    main()
