# A simple Array class for storing elements at specific indices.
class Array:
    def __init__(self, size):
        """Create an array of a specified size."""
        self._items = [None] * size
        self._size = size

    def __getitem__(self, index):
        """Return the element at index."""
        if 0 <= index < self._size:
            return self._items[index]
        else:
            raise IndexError("Array index out of range")

    def __setitem__(self, index, value):
        """Set the element at index to value."""
        if 0 <= index < self._size:
            self._items[index] = value
        else:
            raise IndexError("Array index out of range")

    def __len__(self):
        """Return the size of the array."""
        return self._size

    def clear(self, value=None):
        """Clear the array by setting all elements to value."""
        for i in range(self._size):
            self._items[i] = value
