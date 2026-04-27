import random

class getValues():
    pass

def binaryRecursion(mlist, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2

    if mlist[mid] == target:
        return mid
    elif mlist[mid] > target:
        return binaryRecursion(mlist, target, low, mid - 1)
    else:
        return binaryRecursion(mlist, target, mid +1, high)

mlist = random.sample(range(1,20),10)
mlist = sorted(mlist)
print(mlist)
target = int(input("Enter a number to search : "))
result = binaryRecursion(mlist, target, 0, len(mlist) - 1)
if result != -1:
    print(f"The item found at Index {result} is {mlist[result]}")
else:
    print("Not Found")