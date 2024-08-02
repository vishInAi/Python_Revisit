#Nested if Testing
str="GF Honesty Checker"
print(str.center(50,"."))
print("GF Location(h,b,c,u): ")
print("""
h = Home
b = Bestfriend House
c = College
u = Unknown Location
      """)
loc=input("Location Status: ")
if(loc=='h'):
    print("dont call her parents may pick up")    
elif(loc=='b'):
    print("Call her")
    cStatus=int(input("If she picks press 1 else 0 : "))
    if(cStatus==1):
        print("she loves you")
        if(cStatus==0):
            print("Bestfriend parents may be nearby")
elif(loc=='c'):
    print("Call her")
    cStatus=int(input("If she picks press 1 else 0 : "))
    if(cStatus==1):
        print("she loves you")
        if(cStatus==0):
            print("Keep a Check she may cheat")
elif(loc=='u'):
    print("Call her")
    cStatus=int(input("If she picks press 1 else 0 : "))
    if(cStatus==1):
        print("she loves you")
        if(cStatus==0):
            print("Lol she Dumped ya for another Guy")
else:
    print("Silly you Don't have a GF")

