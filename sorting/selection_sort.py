"""
Selection Sort
Time Complexity = O(n^2)
Space = O(1)
Stability = No (swapping can move equal elts past each other)

Description:
Repeatedly select the smallest element from the unsorted portion of the list and swap it with the 
first element of the unsorted portion (for ascending order).

Steps:
1. Start from the first index i = 0
2. Find the index min_idx of the smallest element in the subarray i -> n-1
3. Swap arr[i] and arr[min_idx]
4. Increment i and repeat until the list is sorted
"""

from sorting_benchmark import basic_benchmark, basic_test

def selection_sort(arr: list[int]):

    n = len(arr)

    # Outer loop
    for i in range(0, n):

        # Find minimum of subarray i -> n - 1
        min = float('inf')
        min_idx = 0

        for j in range(i, n):
            
            if arr[j] < min:
                min = arr[j]
                min_idx = j
        
        # Swap arr[i] and arr[min_idx]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
        
    
    return arr


# Run basic test
basic_test(selection_sort)

# Run basic benchmark
n1 = int(1e2)
n2 = int(1e3)
basic_benchmark(n1, n2, selection_sort)
print("Rather nicely we see that the time has scaled by a factor of roughly 100 when the input scaled by a factor of 10, which is O(n^2)!")