# we'll be studying libraries and will start with random library
import random #imports all functions of the module
from random import choice #imports only declared fuctions

coin = random.choice(["heads", "tails"])

print(coin)

num = random.randint(1,10)

print(num)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

# Lib : Statistics

import statistics

print(statistics.mean([100,90]))

# lib : sys

import sys

# check for errors
if len(sys.argv) < 2:
    sys.exit("too less arguments")
# uncomment below to set a limit of two elements
#elif len(sys.argv) > 2:
#    sys.exit("too many arguments")

# print name tags
    # we can limit from here as well like sys.argv[index] index upto which it can show now and we can slice too 💀
for arg in sys.argv[1:]: # will print every arg from the index 1 to end
    print("hello, my name is", arg)

print("\nfirst loop end\n")

for arg in sys.argv[:2]: # will print upto index 2 from 0
    print("hello, my name is", arg)

print("\nsecond loop end\n")


for arg in sys.argv[1:-2]: # will print from index 1 to 2nd 
    print("hello, my name is", arg)

print("\nthird loop end\n")

