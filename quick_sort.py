import random


#
# def quick_sort(arr):
#     if len(arr) > 1:
#         x = arr[random.randint(0, len(arr) - 1)]
#         low = [i for i in arr if i < x]
#         eq = [i for i in arr if i == x]
#         high = [i for i in arr if i > x]
#         arr = quick_sort(low) + eq + quick_sort(high)
#
#     return arr

# Quick sort in Python

# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = random.randint(0, len(array) - 1)

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quick_sort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
