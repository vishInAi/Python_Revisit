def main():
    print("Waiter : Just Give me my MANeyyy! \n")
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars/100 * percent
    print(f"leave ${tip:.2f}")

def dollars_to_float(d):
    maneyy = d.lstrip("$")
    maneyy = float(maneyy)
    return maneyy

def percent_to_float(p):
    pt = p.rstrip("%")
    pt = float(pt)
    return pt

main()
