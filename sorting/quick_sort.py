"""
Quick Sort
------------
Time Complexity = Average O(n log n) (same as merge), Worst O(n^2) (bubble, insertion, selection, etc)
Space = O(log n) (from recursive function calls, local variables, return addresses etc)
Stable = No (random pivot)

Description:
Divide and conquer algorithm similar to merge sort but sorting in place. The idea is to pick a pivot element,
then split into a left array of all elements smaller than the pivot and a right array of all elements larger 
than the pivot. Then recursively sort both sides. Then the pivot will be in the right position! Between the left and right.
Generally quick sort is faster than merge sort in practise as better cache behavior and low overhead.  

Steps:
1. Pick a pivot element
2. Partition array with left being all elements less than pivot, right being all elements greater than pivot
3. Recursively sort both sides
"""

import random
from sorting_benchmark import basic_test, basic_benchmark

def quick_sort(arr: list[int], low = 0, high = None):

    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        # Random pivot
        pivot_idx = random.randint(low, high)
        pivot = arr[pivot_idx]

        # Swap the pivot for the elt at index high then proceed as normal
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]

        i = low - 1 # Pointer for smaller elements

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                # Swap i and j, as j belongs in low end
                arr[i], arr[j] = arr[j], arr[i]

        # Swap i + 1 and high as the pivot belongs inbetween the left and right arrays 
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        # Return index of pivot
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr

# Basic test
basic_test(quick_sort)

# Basic benchmark
n1 = int(1e3)
n2 = int(1e4)
basic_benchmark(n1, n2, quick_sort)
print(f"Again for a 10 fold increase in the input size we expect a roughly 10*(1+ log 10/log n1) = 12.5 increase in time, we have an around 20 fold increase like merge sort this could be caused by python overhead rather than algorithm time complexity.")

