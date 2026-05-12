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
while current is not None and current.data < value:
    current = current.next

# Deletion
while current is not None and current.data != target:
    current = current.next