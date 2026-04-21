import random

def linearSearch(mlist, target):
    for i in range(len(mlist)):
        if mlist[i] == target:
            return i

    return -1

mlist = random.sample(range(-5,10),10)
print(mlist)
target = int(input("Enter a number to search : "))
result = linearSearch(mlist, target)
if result != -1:
    print(f"The item found at Index {result} is {mlist[result]}")
else:
    print("Not Found")


