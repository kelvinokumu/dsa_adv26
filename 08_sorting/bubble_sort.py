import random

def bubble_sort(unsorted_list):
    number_of_elements = len(unsorted_list)
    for outer_loop in range(number_of_elements):

        for inner_loop in range(number_of_elements-outer_loop - 1):
            if unsorted_list[inner_loop] > unsorted_list[inner_loop + 1]:
                temp = unsorted_list[inner_loop]
                unsorted_list[inner_loop] = unsorted_list[inner_loop + 1]
                unsorted_list[inner_loop + 1] = temp

            print(unsorted_list)

                # unsorted_list[inner_loop], unsorted_list[inner_loop + 1] = unsorted_list[inner_loop + 1], unsorted_list[inner_loop]
    return unsorted_list

def getValues():
    unsorted_list = random.sample(range(50, 100),10)
    unsorted_list = [5,4,3,2,1]
    print(f"Unsorted list {unsorted_list}")
    sorted_list = bubble_sort(unsorted_list)
    # print(sorted_list)
getValues()