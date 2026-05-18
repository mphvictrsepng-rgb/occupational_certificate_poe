import math


# 1.1 - Evaluate 6!
result_1_1 = math.factorial(6)        

# 1.2 - Evaluate 5! / (5-3)!
# = 5! / 2! = 120 / 2 = 60         
result_1_2 = math.factorial(5) / math.factorial(5 - 3)

# 1.3 - Evaluate 7! / (7! * (7-2)!)
# = 7! / (7! * 5!) = 1 / 5! = 1 / 120
result_1_3 = math.factorial(7) / (math.factorial(7) * math.factorial(7 - 2))

# 1.4 - Evaluate 33! / 31!
# = 33 * 32 = 1056
result_1_4 = math.factorial(33) / math.factorial(31)

# 1.5 - Evaluate 0! / 2^2
# = 1 / 4 = 0.25
result_1_5 = math.factorial(0) / (2 ** 2)

# 1.6 - Evaluate 4! - 3!
# = 24 - 6 = 18
result_1_6 = math.factorial(4) - math.factorial(3)

# all results
print("1.1 - 6! =", result_1_1)
print("1.2 - 5! / (5-3)! =", result_1_2)
print("1.3 - 7! / (7! * (7-2)!) =", result_1_3)
print("1.4 - 33! / 31! =", result_1_4)
print("1.5 - 0! / 2^2 =", result_1_5)
print("1.6 - 4! - 3! =", result_1_6)
