"""
Sorting Benchmark
-------------------

This will just give a simple custom benchmark for the sorting algorithms so we can see how time grows with input size

Note usec stands for microsecond so 10^-6 of a second
"""

import timeit
import random

def basic_benchmark(n1: int, n2: int, func, *args, **kwargs):
 
    # Set random seed for reproducibility
    random.seed = 37

    # Take an average time for 100 different random lists of length n1 and n2
    time_taken_n1 = timeit.timeit(lambda: func([random.randint(-100, 100) for _ in range(n1)], *args, **kwargs), number = 100)
    time_taken_n2 = timeit.timeit(lambda: func([random.randint(-100, 100) for _ in range(n2)], *args, **kwargs), number = 100)
    print(f"Average time over 100 runs for a length {n1} array: {time_taken_n1} usec")
    print(f"Average time over 100 runs for a length {n2} arrray: {time_taken_n2} usec")
    print(f"This has increased by a factor of {time_taken_n2 / time_taken_n1} whilst the input has increased by a factor of {n2/n1}")

def basic_test(func, *args, **kwargs):

    test_array = [random.randint(-100, 100) for _ in range(10)]
    print(test_array)
    sorted = func(test_array, *args, **kwargs)
    # Ascending
    print(sorted)
    # Descending
    print(sorted[::-1])