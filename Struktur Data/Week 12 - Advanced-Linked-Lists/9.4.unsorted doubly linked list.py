# Traversal
current = head

while current is not None:
    print(current.data)
    current = current.next
    
# Search
current = head
while current is not None and current.data != target:
    current = current.next
    
# Insertion
newNode = Node(value)
newNode.next = head
head.prev = newNode
head = newNode

# Deletion
current = head
while current is not None and current.data != target:
    current = current.next
if current is not None:
    current.prev.next = current.next
    if current.next is not None:
        current.next.prev = current.prev