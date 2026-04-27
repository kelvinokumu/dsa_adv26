import random

def max_min(list_of_values):
    minimum = list_of_values[0]
    for num in list_of_values:
        if num > minimum:
            minimum = num

    return minimum

def getValues():
    list_of_values = [1,2,3,4,5,6]
    list_of_values = random.sample(range(70, 100),10)
    print(f"List of values {list_of_values}")
    print(max_min(list_of_values))
    # print(f"Values is {result}")
getValues()





