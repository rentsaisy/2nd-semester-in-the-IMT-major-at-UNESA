current = head
prev = None

while True:

    if current.data == target:
        break

    prev = current
    current = current.next

    if current == head:
        current = None
        break

if current is not None:

    if current == head:

        tail = head

        while tail.next != head:
            tail = tail.next

        if head.next == head:
            head = None
        else:
            tail.next = head.next
            head = head.next

    else:
        prev.next = current.next