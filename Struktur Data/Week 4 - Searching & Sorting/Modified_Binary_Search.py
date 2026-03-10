def findFirst(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1   # search left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result


def findLast(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1   # search right side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result


def countOccurrences(sortedList, target):
    first = findFirst(sortedList, target)
    
    if first == -1:
        return 0
    
    last = findLast(sortedList, target)
    
    return last - first + 1


# Example
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 4))  # 4
print(countOccurrences([1, 2, 4, 4, 4, 4, 7, 9, 12], 5))  # 0