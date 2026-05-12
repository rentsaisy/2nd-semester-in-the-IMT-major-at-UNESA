# Traversal
current = rowHead

while current is not None:
    print(current.value)
    current = current.nextCol
    
# Search
current = rowHead

while current is not None and current.col != targetCol:
    current = current.nextCol
    
# Insertion
while current is not None and current.col < newCol:
    current = current.nextCol
    
# Deletion
while current is not None and current.col != targetCol:
    current = current.nextCol