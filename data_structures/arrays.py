"""
Arrays
-------
Basic operations, in python arrays are dynamic lists so not of fixed length like C/C++
Continous memory: elts are stored one after the other in memory. 
Dynamic resizing: when capacity is exceeded python will allocate a new larger array and copy elts over
Heterogenous types allowed: in python arrays you can mix types
"""

import bisect

arr = [1, 2, 3, 4, 5]

# Lookup
# Time complexity = O(1)
arr[3] 

# Update
# Time complexity = O(1)
arr[3] = 7

# Append
# Time complexity = O(1), may be O(n) if resizing
arr.append(8)

# Insert (at end)
# Time complexity = O(1), may be O(n) if resizing
arr.insert(len(arr), 9)

# Insert (at index)
# Time complexity = O(n), elts must be shifted to the right
arr.insert(2, 10) # 2 is index, 10 is value

# Delete by index
# Time complexity = O(n), shift elts left to fill gap
del arr[3]

# Delete by value
# Time complexity = O(n), must search elts for the element first
arr.remove(10) 

# Search (unsorted)
# Time complexity = O(n), linear scan
3 in arr

# Search (sorted, binary)
# Time complexity = O(log n), binary search algorithm
arr[2] = 3
arr.sort()
print(bisect.bisect_left(arr, 3))

# Length
# Time complexity = O(1), stored internally, so I guess O(n) to inital compute
len(arr)

# Iteration
# Time complexity = O(n)
for x in arr:
    continue

# Copy
# Time complexity = O(n)
# Notes: creates shallow copy
arr.copy() 
# or
arr[:]

# Slicing
# Time complexity = O(k)
# Notes: copies a slice of size k
arr[2:5] # doesn't include 5

# Concateneation
# Time complexity = O(n+m)
# Notes: creates new list
arr2 = [2, 3, 4]


# Extend another list
# Time complexity = O(m)
# Notes: adds m elts in place
arr.extend(arr2)

# Reverse
# Time complexity = O(n)
# Notes: in place reversal
arr.reverse()
# or
arr[::-1]

# Sort
# Time complexity = O(n log n)
# Notes: Timsort algorithm (stable)
arr.sort()
