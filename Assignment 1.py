import time
import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sizes = [100, 200, 800]

print("Sorting Performance Comparison:\n")

for size in sizes:
    data = random.sample(range(size * 10), size)

    # Selection Sort Timing
    s_data = data[:]
    start = time.time()
    selection_sort(s_data)
    selection_time = time.time() - start

    # Insertion Sort Timing
    i_data = data[:]
    start = time.time()
    insertion_sort(i_data)
    insertion_time = time.time() - start

    print(f"Size: {size}")
    print(f"Selection Sort Time: {selection_time:.6f} seconds")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print("-----------------------------")




