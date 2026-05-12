current = head

while current is not None and current.data < target:
    current = current.next

if current is not None and current.data == target:

    if current.prev is not None:
        current.prev.next = current.next
    else:
        head = current.next

    if current.next is not None:
        current.next.prev = current.prev