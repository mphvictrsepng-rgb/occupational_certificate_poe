# 1.1 This function rounds all numbers in the list to the nearest 10

def round_to_ten(numbers):

    i = 0  # starting index

    while i < len(numbers):

        # round each number to the nearest 10
        numbers[i] = round(numbers[i] / 10) * 10

        i += 1  # move to the next number

    return numbers


# Example
print(round_to_ten([12, 25, 47, 83]))

# 1.2 This function increases numbers less than 40 by 2
# It also counts how many numbers in the new list are less than 50

def increment_numbers(numbers):

    new_list = []       # store updated numbers
    count = 0           # count numbers less than 50

    i = 0     # starting index

    while i < len(numbers):

        num = numbers[i]

        # add 2 if number is less than 40
        if num < 40:
            num += 2

        new_list.append(num)

        # count numbers less than 50
        if num < 50:
            count += 1

        i += 1  # move to next number

    return (new_list, count)


# an example
print(increment_numbers([10, 25, 40, 60]))