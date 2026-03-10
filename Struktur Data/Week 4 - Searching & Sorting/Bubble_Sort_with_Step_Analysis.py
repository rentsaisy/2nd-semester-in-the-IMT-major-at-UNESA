def bubbleSort(arr):
    arr = arr.copy()
    n = len(arr)
    
    total_comparisons = 0
    total_swaps = 0
    passes_used = 0

    for i in range(n):
        swapped = False
        passes_used += 1

        for j in range(0, n - i - 1):
            total_comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                total_swaps += 1
                swapped = True

        print(f"Pass {passes_used}: {arr}")

        if not swapped:  # early termination
            break

    return (arr, total_comparisons, total_swaps, passes_used)


# Test cases
print(bubbleSort([5, 3, 4, 2, 8]))
print(bubbleSort([1, 2, 3, 4, 5]))