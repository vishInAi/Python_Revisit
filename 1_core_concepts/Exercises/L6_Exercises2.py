# write a recursive function to calculate the sum of first n natural numbers.

def num(n):
    if (n == 0):
        return 0
    return num(n-1) + n

sum = num(5)
print(sum)

# write a recursive function to print all elements in a list
idx = 0
list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
def num(list,idx):
    if (idx == len(list)):
        return
    print(list[idx])
    num(list, idx+1)

num(list,idx)

    