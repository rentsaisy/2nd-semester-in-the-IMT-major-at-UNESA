from linked_list import LinkedList

class BigInteger:
    def __init__(self, number_str):
        self.digits = LinkedList()
        
        for digit in number_str:
            self.digits.insert_end(int(digit))

    def display(self):
        return self.digits.display()