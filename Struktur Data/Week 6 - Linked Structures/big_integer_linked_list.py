class Node:
    def __init__(self, digit):
        self.digit = digit
        self.next = None

class BigIntegerLL:
    def __init__(self, number):
        self.head = None
        for digit in str(number)[::-1]:  # reverse order
            self.insert(int(digit))

    def insert(self, digit):
        new_node = Node(digit)
        new_node.next = self.head
        self.head = new_node
        
    def print_list(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.digit))
            current = current.next
        return " → ".join(result)

    def display(self):
        current = self.head
        result = ""
        while current:
            result = str(current.digit) + result
            current = current.next
        return result
    
# Run program
num = BigIntegerLL(45839)

print("\nInternal linked list:")
print(num.print_list())

print("\nDisplay output:")
print(num.display())