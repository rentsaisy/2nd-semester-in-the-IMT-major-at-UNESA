import random

def insertionSort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        
        arr[j + 1] = key

    return arr, comparisons + swaps


def selectionSort(arr):
    arr = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, comparisons + swaps


def hybridSort(theSeq, threshold=10):
    arr = theSeq.copy()
    n = len(arr)

    if n < threshold:
        return insertionSort(arr)
    else:
        return selectionSort(arr)
    
# Test cases
sizes = [50, 100, 500]

print(f"{'Size':<10}{'Insertion Ops':<20}{'Selection Ops':<20}{'Hybrid Ops':<20}")

for size in sizes:
    data = [random.randint(1, 1000) for _ in range(size)]

    _, insertion_ops = insertionSort(data)
    _, selection_ops = selectionSort(data)
    _, hybrid_ops = hybridSort(data)

    print(f"{size:<10}{insertion_ops:<20}{selection_ops:<20}{hybrid_ops:<20}")