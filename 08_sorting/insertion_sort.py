import random


def insertion_sort(unsorted_list):
    number_of_elements = len(unsorted_list)

    # Start from the second element (index 1) and move through the list
    for current_index in range(1, number_of_elements):
        current_value = unsorted_list[current_index]
        print(f"Current is {unsorted_list[current_index]}")

        # Move the current value to its correct position in the sorted part
        while unsorted_list[current_index - 1] > current_value and current_index > 0:
            # Swap the current value with the one before it

            temp = unsorted_list[current_index]
            unsorted_list[current_index] = unsorted_list[current_index - 1]
            unsorted_list[current_index - 1] = temp
            # print(f"Sorted {unsorted_list}")

            # numbers[current_index], numbers[current_index - 1] = numbers[current_index - 1], numbers[current_index]

            # move backwards to the beginning
            current_index -= 1  # increment/ decrement
            # current_index = current_index - 1 
            print(f"Sorted {unsorted_list}")

    return unsorted_list


def getValues():
    # unsorted_list = random.sample(range(20,60),5)
    unsorted_list = [59, 55, 50, 31, 26]
    # unsorted_list = [1, 2, 3, 4, 5]
    print(f"Unordered list is : {unsorted_list}")
    sortedlist = insertion_sort(unsorted_list)
    print(f"Sorted list {sortedlist}")

getValues()