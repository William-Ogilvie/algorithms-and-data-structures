"""
Sorting Benchmark
-------------------

This will just give a simple custom benchmark for the sorting algorithms so we can see how time grows with input size

Note usec stands for microsecond so 10^-6 of a second
"""

import timeit
import random

def basic_benchmark(n1: int, n2: int, func, *args, **kwargs):
 
    n1_test_array = [random.randint(-100, 100) for _ in range(n1)]
    n2_test_array = [random.randint(-100, 100) for _ in range(n2)]

    # Time this for the two lists
    time_taken_n1 = timeit.timeit(lambda: func(n1_test_array, *args, **kwargs), number = 1000)
    time_taken_n2 = timeit.timeit(lambda: func(n2_test_array, *args, **kwargs), number = 1000)
    print(f"Average time over 1000 runs for a length {n1} array: {time_taken_n1} usec")
    print(f"Average time over 1000 runs for a length {n2} arrray: {time_taken_n2} usec")
    print(f"This has increased by a factor of {time_taken_n2 / time_taken_n1} whilst the input has increased by a factor of {n2/n1}")

