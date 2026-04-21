import random

def binaryIter(mlist, target):
    low = 0
    high = len(mlist) - 1
    while low <= high:
        mid = (low + high) // 2
        print(f"Low is {mlist[low]}")
        print(f"Mid is {mlist[mid]}")
        print(f"High is {mlist[high]}")
        if mlist[mid] == target:
            return mid
        elif mlist[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

mlist = random.sample(range(-5,1),4)
mlist = sorted(mlist)
print(mlist)
target = int(input("Enter a number to search : "))
result = binaryIter(mlist, target)
if result != -1:
    print(f"The item found at Index {result} is {mlist[result]}")
else:
    print("Not Found")