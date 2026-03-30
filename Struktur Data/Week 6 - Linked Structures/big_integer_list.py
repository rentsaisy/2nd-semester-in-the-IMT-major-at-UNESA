class BigIntegerList:
    def __init__(self, number):
        self.digits = [int(d) for d in str(number)][::-1]

    def display(self):
        return ''.join(map(str, self.digits[::-1]))
    
# Run program
num = BigIntegerList(45839)

print("Input number:", 45839)
print("\nList representation (reversed):")
print(num.digits)

print("\nDisplay output:")
print(num.display())