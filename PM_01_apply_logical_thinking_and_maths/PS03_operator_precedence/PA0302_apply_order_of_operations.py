#i chose to use commments as a form of coding the steps i took to solve each problem, as it is a good way to show the order of operations and how i arrived at the final answer.

# 1.1 - Calculate 2^(2^3)

# First i calculated the inner exponent: 2^3 = 8
# Then: 2^8 = 256
result_1_1 = 2 ** (2 ** 3)

# 1.2 - Calculate 3^(2^0) + 3

# First: 2^0 = 1
# Then: 3^1 = 3
# Finally: 3 + 3 = 6
result_1_2 = 3 ** (2 ** 0) + 3

# 1.3 - Calculate -4^2 + 3
# the exponent comes before negation: 4^2 = 16
# Then: -16
# Finally i added 3 to make it: -16 + 3 = -13
result_1_3 = -(4 ** 2) + 3

# 1.4 - Calculate -5^(2-3) x 5
# First: 2 - 3 = -1
# Then: 5^(-1) = 0.2
# Then: -0.2
# last step i multiplied by 5: -0.2 * 5 = -1
result_1_4 = -(5 ** (2 - 3)) * 5

# 1.5 - Calculate (-3)^3 x 3
# (-3)^3 = -27
# Then i multiplied by 3: -27 * 3 = -81
result_1_5 = (-3) ** 3 * 3

# all answers printed
print("1.1 - 2^(2^3) =", result_1_1)
print("1.2 - 3^(2^0) + 3 =", result_1_2)
print("1.3 - -4^2 + 3 =", result_1_3)
print("1.4 - -5^(2-3) x 5 =", result_1_4)
print("1.5 - (-3)^3 x 3 =", result_1_5)
