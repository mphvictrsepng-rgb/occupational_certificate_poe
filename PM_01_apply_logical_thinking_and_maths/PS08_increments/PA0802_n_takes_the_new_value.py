# 1.2 This function finds the lowest
# and second lowest numbers in a list

def find_lowest(numbers):

    # sort the list from smallest to biggest
    numbers.sort()

    lowest = numbers[0]      # first number
    low = numbers[1]         # second number

    return (lowest, low)


# an xample
print(find_lowest([12, 5, 8, 2, 20]))