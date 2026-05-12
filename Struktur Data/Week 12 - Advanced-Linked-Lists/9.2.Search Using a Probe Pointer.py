current = probe

while current is not None and current.data != target:
    if target < current.data:
        current = current.prev
    else:
        current = current.next