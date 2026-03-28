from big_integer import BigInteger
from operations import add, subtract

num1 = BigInteger("12345678901234567890")
num2 = BigInteger("98765432109876543210")

result_add = add(num1, num2)
result_sub = subtract(num2, num1)

print("Addition:", result_add.display())
print("Subtraction:", result_sub.display())