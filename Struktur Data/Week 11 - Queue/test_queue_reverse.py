"""Test script demonstrating queue reversal functionality."""
from llistqueue import Queue

def print_queue(queue, label):
    """Helper function to print queue contents."""
    items = list(queue)
    print(f"{label}: {items}")


def test_reverse_basic():
    """Test basic queue reversal."""
    print("=" * 60)
    print("TEST 1: Basic Queue Reversal")
    print("=" * 60)
    
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    
    print_queue(q, "Original queue")
    q.reverse()
    print_queue(q, "After reverse")
    print()


def test_reverse_strings():
    """Test queue reversal with strings."""
    print("=" * 60)
    print("TEST 2: Queue Reversal with Strings")
    print("=" * 60)
    
    q = Queue()
    items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    for item in items:
        q.enqueue(item)
    
    print_queue(q, "Original queue")
    q.reverse()
    print_queue(q, "After reverse")
    print()


def test_reverse_empty():
    """Test reversing an empty queue."""
    print("=" * 60)
    print("TEST 3: Reversing Empty Queue")
    print("=" * 60)
    
    q = Queue()
    print_queue(q, "Original empty queue")
    q.reverse()
    print_queue(q, "After reverse (should be empty)")
    print()


def test_reverse_single():
    """Test reversing a single-item queue."""
    print("=" * 60)
    print("TEST 4: Reversing Single-Item Queue")
    print("=" * 60)
    
    q = Queue()
    q.enqueue(42)
    print_queue(q, "Original single-item queue")
    q.reverse()
    print_queue(q, "After reverse (should be unchanged)")
    print()


def test_reverse_twice():
    """Test reversing a queue twice (should return to original)."""
    print("=" * 60)
    print("TEST 5: Double Reversal (should return to original)")
    print("=" * 60)
    
    q = Queue()
    original = list(range(1, 7))
    for item in original:
        q.enqueue(item)
    
    print_queue(q, "Original queue")
    q.reverse()
    print_queue(q, "After first reverse")
    q.reverse()
    print_queue(q, "After second reverse (should match original)")
    print()


def test_reverse_complex_objects():
    """Test reversing queue with complex objects."""
    print("=" * 60)
    print("TEST 6: Queue Reversal with Complex Objects")
    print("=" * 60)
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person({self.name}, {self.age})"
    
    q = Queue()
    people = [
        Person("Alice", 25),
        Person("Bob", 30),
        Person("Charlie", 35),
    ]
    for person in people:
        q.enqueue(person)
    
    print_queue(q, "Original queue")
    q.reverse()
    print_queue(q, "After reverse")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("QUEUE REVERSAL FUNCTION TESTS")
    print("=" * 60 + "\n")
    
    test_reverse_basic()
    test_reverse_strings()
    test_reverse_empty()
    test_reverse_single()
    test_reverse_twice()
    test_reverse_complex_objects()
    
    print("=" * 60)
    print("All tests completed!")
    print("=" * 60)
