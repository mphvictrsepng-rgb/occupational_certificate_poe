#1.1
def repeating(n):

    if n == 0 or n == 1:
        return

    if n % 4 == 0:
        print("Ping", end=" ")
        repeating(n - 1)

    elif n % 2 == 0:
        print("Pong", end=" ")
        repeating(n - 2)

    elif n % 3 == 0:
        print("King", end=" ")
        repeating(n - 3)

    elif n % 5 == 0:
        print("Donkey", end=" ")
        repeating(n - 5)

    else:
        print("Kong", end=" ")
        repeating(n - 4)


# testing
repeating(13)

print('..')    # i added this to separate the outputs of different functions

#1.2
def repeating(n):

    if n == 0 or n == 1:
        return

    if n % 4 == 0:
        print("Ping", end=" ")
        repeating(n - 1)

    elif n % 2 == 0:
        print("Pong", end=" ")
        repeating(n - 2)

    elif n % 3 == 0:
        print("King", end=" ")
        repeating(n - 3)

    elif n % 5 == 0:
        print("Donkey", end=" ")
        repeating(n - 5)

    else:
        print("Kong", end=" ")
        repeating(n - 4)


# testing the function
repeating(15)

print('..')   

#1.4
# This function checks if a number is even

def is_even(n):

    # even numbers give remainder 0
    if n % 2 == 0:
        return True

    return False

# e.g., to test
print(is_even(8))


#1.5
# This function checks if a number is prime

def is_prime(n):

    # numbers less than 2 are not prime
    if n < 2:
        return False

    for i in range(2, n):    # check for factors

        if n % i == 0:
            return False

    return True


# example
print(is_prime(7))