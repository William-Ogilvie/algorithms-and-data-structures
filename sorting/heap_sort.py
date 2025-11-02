"""
Heap Sort
------------
Time Complexity = O(n log n) (Heapify takes log n need to do n times)
Space = O(1) (in-place)
Stable = No 

Description:
Heap sort works by turing the list into a binary heap (which is a binary heap that is complete, 
ever level filled except last, and obeys heap property for max heap that means every 
parent \\ge its children). Then build a max heap from the list, repeatedly extract the largest element
(root of the heap) and put it at the end of the list. Heapify the remaining part again to restore the heap
property.

Heaps themselves are just stored as flat arrays with special indexing rules for children:
For any node at index i:
left child = 2i + 1
right child = 2i +2
parent = floor((i-1)/2)

Heapifying means take a parent and its two children, if there is a larger child swap with parent and heapify on child recursively.
This will restore the heap property. 

To build a heap heapify on the last parent n // 2 - 1, then heapify on all parents above this.

e.g. i = 0 left child = 1, right = 2. If i = 5 parent = 2

So [10, 5, 3, 2, 4] becomes

     10
    5    3
   2  4

Steps:
1. Build a max heap from the list
2. Repeatedly extract the largest element (root of the heap) and put it at the end of the list
3. Heapify the remaining part again to restore the heap property
"""

def heapify(arr, n, i):
    """
    The idea of heapifying is say some element doesn't satisfy the heap property, you then look at it's children 
    and swap the largest child if needed and continue recursively heapifying the children until you reached the end of the tree
    """

    largest = i
    left = 2*i + 1 
    right =  2*i + 2

    # Find the max of the parent, left child and right child
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
    

test_array = [3, 4, 10, 2, 5]
print(test_array)
# Build by heapifying on parent upwards
for i in range(len(test_array) // 2 - 1, -1, -1):
    heapify(test_array, len(test_array), i)
print(test_array)




