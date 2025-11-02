"""
Bubble Sort
-------------
Time Complexity = O(n^2)
Space = O(1)
Stable = Yes (elts with equal keys appear in same relative order in output as in input)

Description:
Bubble sort is a simple sorting algorithm where you repeatedly loop through the array swaping adjacent elements into the correct order
(i.e. ascending or descending). Stop once there are no more adjacent pairs to swap, it is named bubble sort because largest/smallest elements will bubble up 
to the front of the array.

Steps:
1. Define an outer loop of length n
2. Pass through the array swapping adjacent elements in the wrong order
3. Track whether we swapped an element on each pass through
4. Break out of the outer loop early if we didn't swap anything
"""

import timeit
import random


def bubble_sort(arr: list[int]):
    n = len(arr)

    # We need a double loop here of length n, the intution is that each pass of bubble sort will place one
    # element into the correct position, there are n elements so we need to pass through the array at most n times
    for i in range(0, n):
        # Perform a pass of the bubble sort alogirthm through the array, keep track of whether or not we have swapped a pair at all
        
        # Keep track of if we performed a swap this run through 
        swapped = False

        # We don't have to go all the way to the end, by the ith iteration of the outer loop we will have bubled up i elements to the end of the array
        for j in range(0, n - i - 1):

            # Check if jth element is larger than (j+1)th element, if true swap elts 
            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1], arr[j] 
                # Remember we have swapped a pair
                swapped = True

        # Optimisation if we didn't swap any pairs then we know the list is sorted and can break early
        if not swapped:
            break
    
    return arr

test_array = [3, 5, 1, 9, 4, 3, 2, 13, -4, -1]
sorted = bubble_sort(test_array)
# To get descending order just reverse at the end (technically this will add O(n) extra time)
reverse_sorted = sorted[::-1] # start stop step, so start at start of list, end at end but step backwards
# Print ascending order
print(sorted)
# Print descending order
print(reverse_sorted)

# Time for benchmarking and to show O(n^2)
time_taken = timeit.timeit(lambda: bubble_sort(test_array), number = 1000)
print(f"Average time over 1000 runs for a length 10 array: {time_taken} usec")

# Length of larger lists
n1 = int(1e2)
n2 = int(1e3)

# Time this for 100 runs on 100 random lists of length n1 and n2 respectively
time_taken_medium = timeit.timeit(lambda: bubble_sort([random.randint(-100, 100) for _ in range(n1)]), number = 100)
time_taken_larger = timeit.timeit(lambda: bubble_sort([random.randint(-100, 100) for _ in range(n2)]), number = 100)
print(f"Average time over 100 runs for a length {n1} array: {time_taken_medium} usec")
print(f"Average time over 100 runs for a length {n2} arrray: {time_taken_larger} usec")
print(f"This has increased by a factor of {time_taken_larger / time_taken_medium} whilst the input has increased by a factor of 10")
print(f"We see roughly 100 fold growth in time taken so O(n^2) as expected!")

        
