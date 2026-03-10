def mergeThreeSortedLists(listA, listB, listC):
    i = j = k = 0
    result = []

    while i < len(listA) or j < len(listB) or k < len(listC):
        a = listA[i] if i < len(listA) else float('inf')
        b = listB[j] if j < len(listB) else float('inf')
        c = listC[k] if k < len(listC) else float('inf')

        if a <= b and a <= c:
            result.append(a)
            i += 1
        elif b <= a and b <= c:
            result.append(b)
            j += 1
        else:
            result.append(c)
            k += 1

    return result


# Example
print(mergeThreeSortedLists([1, 5, 9], [2, 6, 10], [3, 4, 7]))