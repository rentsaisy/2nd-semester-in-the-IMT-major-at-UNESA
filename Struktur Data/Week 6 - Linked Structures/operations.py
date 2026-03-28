from big_integer import BigInteger

def add(num1, num2):
    # Convert to string for simplicity (can be improved later)
    result = str(int(num1.display()) + int(num2.display()))
    return BigInteger(result)


def subtract(num1, num2):
    result = str(int(num1.display()) - int(num2.display()))
    return BigInteger(result)