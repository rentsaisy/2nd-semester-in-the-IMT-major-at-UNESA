# Function
def deduplication(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Input
data = [1, 2, 2, 3, 4, 3, 5, 1]
print(deduplication(data))