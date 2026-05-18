
import math

# 1.1 - 6/3(1+2)
result_1_1 = 6 / 3 * (1 + 2)         # Parentheses first, then division and multiplication from left to right

# 1.2 - 1/4 ((2^3) + 4x2)
result_1_2 = 1 / 4 * ((2 ** 3) + 4 * 2)   # Exponents first, then multiplication, then addition, and finally division

# 1.3 - 2^(2)^4 - 5^2 / sqrt(4^2 + 3^2) + 2^(2-(4/2) - 1)
# the exponents are done first, then division, then addition/subtraction
result_1_3 = 2 ** (2 ** 4) - 5 ** 2 / math.sqrt(4 ** 2 + 3 ** 2) + 2 ** (2 - (4 / 2) - 1)

# the results to check
print("1.1 - 6/3(1+2) =", result_1_1)
print("1.2 - 1/4 ((2^3)+4x2) =", result_1_2)
print("1.3 - expression =", result_1_3)
