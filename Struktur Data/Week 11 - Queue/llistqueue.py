# A linked list-based queue implementation.
class _QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        """Create an empty queue."""
        self._front = None
        self._rear = None
        self._count = 0

    def enqueue(self, data):
        """Add an element to the rear of the queue."""
        node = _QueueNode(data)
        if self._front is None:
            self._front = node
        else:
            self._rear.next = node
        self._rear = node
        self._count += 1

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self._front is None:
            raise IndexError("dequeue from empty queue")
        data = self._front.data
        self._front = self._front.next
        self._count -= 1
        if self._front is None:
            self._rear = None
        return data

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._count == 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._count

    def __iter__(self):
        """Iterate through the queue elements."""
        current = self._front
        while current is not None:
            yield current.data
            current = current.next

    def reverse(self):
        """Reverse the order of items in the queue.
        
        This method uses a stack-based approach:
        1. Dequeue all items and push to stack
        2. Pop from stack and enqueue back to queue
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if self._count <= 1:
            return  # No reversal needed for empty or single-item queue
        
        stack = []
        # Dequeue all items and push to stack
        while not self.is_empty():
            stack.append(self.dequeue())
        
        # Pop from stack and enqueue back
        while stack:
            self.enqueue(stack.pop())
