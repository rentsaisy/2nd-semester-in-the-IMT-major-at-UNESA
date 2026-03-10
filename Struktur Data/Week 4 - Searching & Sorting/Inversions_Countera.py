import random
import time

# a) Naive O(n^2) inversion counter
def countInversionsNaive(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


# b) Smart inversion counter using Merge Sort O(n log n)
def mergeAndCount(left, right):
    merged = []
    i = j = inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count


def mergeSortAndCount(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = mergeSortAndCount(arr[:mid])
    right, inv_right = mergeSortAndCount(arr[mid:])

    merged, inv_merge = mergeAndCount(left, right)

    return merged, inv_left + inv_right + inv_merge


def countInversionsSmart(arr):
    _, count = mergeSortAndCount(arr)
    return count


# Testing and timing
sizes = [1000, 5000, 10000]

print(f"{'Size':<10}{'Naive Time (s)':<20}{'Smart Time (s)':<20}{'Same Result'}")

for size in sizes:
    data = [random.randint(1, 100000) for _ in range(size)]

    start = time.time()
    naive = countInversionsNaive(data)
    naive_time = time.time() - start

    start = time.time()
    smart = countInversionsSmart(data)
    smart_time = time.time() - start

    print(f"{size:<10}{naive_time:<20.5f}{smart_time:<20.5f}{naive == smart}")