"""
Merge Sort
------------
Time Complexity = O(n log n) (each merge step linear O(n) and there are O(log n) levels, bc split in 1/2 each time
Space = O(n) (temporary lists)
Stable = Yes

Description:
Merge sort works by recursively splitting the array into two halves until we are down to single element arrays. 
Then merge sort "merges" these smaller arrays together in order, repeating until we have the full sorted array.
This is essentially a divide and conquer approach.

Steps:
1. Recursively split the array in half until you have n (len(arr)) inidivdual arrays
2. Merge these smaller arrays ordering as you merge until you have the full sorted array
"""

import random
from sorting_benchmark import basic_benchmark

def merge(left, right):

    # Store merged result
    result = []
    
    # We know left and right are both already sorted so we just need to keep mergin until one of them is empty
    while left != [] and right != []:

        # If the first element of left is less than or equal to that of the right then append to result
        if left[0] <= right[0]:
            result.append(left[0])

            # Remove this elt from left
            left.pop(0)
        else:
            result.append(right[0])

            # Remove this elt from right
            right.pop(0)
    
    # We have now broken from the loop meaning one of left or right is empty
    if left == []:
        result += right
    else:
        result += left

    return result

def merge_sort(arr: list[int]):
    # We do ascending by default, just reverse for descending

    # If array is just one element return it 
    if len(arr) == 1:
        return arr

    # Split the array roughly in half
    split_val = len(arr) // 2 # floor division rounding towards -infty
    left_array = arr[:split_val]
    right_array = arr[split_val:]

    # Merge sort the LHS
    left_sorted = merge_sort(left_array)
    # Merge sort the RHS
    right_sorted = merge_sort(right_array)

    # Returned the merged left and right halves
    return merge(left_sorted, right_sorted)



test_array = [random.randint(-100, 100) for _ in range(10)]
print(test_array)
sorted = merge_sort(test_array)
# Ascending
print(sorted)
# Descending
print(sorted[::-1])

# Run basic benchmark
n1 = int(1e3)
n2 = int(1e4) 
basic_benchmark(n1, n2, merge_sort)
print(f"10 (1 + log 10 / log n1) is approx 13.33, the experimental factor we got is about 56, this is much larger and may be to do with python overhead rather than the algorithm iteslf.")
