"""
Insertion Sort
----------------
Complexity = O(n^2), O(n) if array almost sorted
Sapce = O(1) (in place)
Stable = Yes

Description:
Insertion sort is a simple sorting algorithm where you take each element in the list and insert it into the correct
position among all previous elements.

Steps:
1. Start from second element (i=1)
2. Take the element and call it key
3. Compare backwards with elements in the sorted part (indices < i)
4. Shift larger elements one position to the right
5. Inert key into its correct place.
6. Move to next element, repeat until the array ends.
"""

import random
from sorting_benchmark import basic_benchmark

def insertion_sort(arr: list[int]):

    n = len(arr)

    for i in range(1, n):
        # Get ith element 
        key = arr[i]
        
        # Loop through the previous i-1 elements inserting key into the correct position
        for j in range(0, i):
            # Check if the current index is larger than the key 
            if arr[j] > key:
                # Now insert key at index j shifting all other elements one index to the right
                for k in range(i, j, -1):
                    arr[k] = arr[k-1]
                
                arr[j] = key

                break
    return arr

test_array = [random.randint(-100, 100) for _ in range(10)]
print(test_array)
sorted = insertion_sort(test_array)
# Ascending
print(sorted)
# Descending
print(sorted[::-1])

# Run a basic benchmark, n1 = 1e3, n2 = 1e4
basic_benchmark(int(1e2), int(1e3), insertion_sort)
