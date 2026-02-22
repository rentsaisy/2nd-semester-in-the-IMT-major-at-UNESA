# Function
def intersection(arr1, arr2):
    set2 = set(arr2)
    result = []
    
    for item in arr1:
        if item in set2 and item not in result:
            result.append(item)
    
    return result

# Input
a = [1, 2, 2, 3, 4]
b = [2, 3, 5]

print(intersection(a, b))