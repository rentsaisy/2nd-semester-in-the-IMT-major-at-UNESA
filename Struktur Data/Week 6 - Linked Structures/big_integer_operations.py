class BigInteger:
    def __init__(self, number):
        self.value = int(number)

    # Arithmetic operators
    def __iadd__(self, other):
        self.value += other.value
        return self

    def __isub__(self, other):
        self.value -= other.value
        return self

    def __imul__(self, other):
        self.value *= other.value
        return self

    def __ifloordiv__(self, other):
        self.value //= other.value
        return self

    def __imod__(self, other):
        self.value %= other.value
        return self

    def __ipow__(self, other):
        self.value **= other.value
        return self

    # Bitwise operators
    def __ilshift__(self, other):
        self.value <<= other.value
        return self

    def __irshift__(self, other):
        self.value >>= other.value
        return self

    def __ior__(self, other):
        self.value |= other.value
        return self

    def __iand__(self, other):
        self.value &= other.value
        return self

    def __ixor__(self, other):
        self.value ^= other.value
        return self

    def __str__(self):
        return str(self.value)


# MAIN PROGRAM
A = BigInteger(1000)
B = BigInteger(200)

print("Initial values:")
print("A =", A)
print("B =", B)

A += B
print("\nAfter A += B:")
print("A =", A)

A -= B
print("\nAfter A -= B:")
print("A =", A)

A *= B
print("\nAfter A *= B:")
print("A =", A)

A //= B
print("\nAfter A //= B:")
print("A =", A)

A %= B
print("\nAfter A %= B:")
print("A =", A)

A **= BigInteger(2)
print("\nAfter A **= 2:")
print("A =", A)

A <<= BigInteger(1)
print("\nAfter A <<= 1:")
print("A =", A)

A >>= BigInteger(1)
print("\nAfter A >>= 1:")
print("A =", A)

A |= B
print("\nAfter A |= B:")
print("A =", A)

A &= B
print("\nAfter A &= B:")
print("A =", A)

A ^= B
print("\nAfter A ^= B:")
print("A =", A)