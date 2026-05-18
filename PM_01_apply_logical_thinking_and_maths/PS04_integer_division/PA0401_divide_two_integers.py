
# 1.1 - distribute_n should split n into k positive parts


def distribute_n(n, k):               # If n < k then it's impossible to give at least 1 to each
    if n < k:
        return None           
    base = n // k                # Integer division will give the base size of each part
    remainder = n % k           # The remainder will be distributed as 1 extra to the first 'remainder' parts
    
    result = [base] * k         #base size for each part
    for i in range(remainder):    # Distribute the remainder by adding 1 to the first 'remainder' parts. plus i used "for" loop to iterate through the first 'remainder' parts and add 1 to each of them
        result[i] += 1
    return result


# 1.2 - pie_chart converts percentage values into 360-degree shares
# it only works when the list sums to exactly 100

def pie_chart(percentages):
    if abs(sum(percentages) - 100) > 1e-9:       #1e-9 is a small threshold to account for floating-point precision issues. If the sum of the percentages is not close enough to 100, the function will return None, indicating an error in the input.
        return None
    result = []                 # The function initializes an empty list called result to store the output
    for p in percentages:        
        share = p * 360 / 100
        result.append((p, share))    
    return result


# 1.3 - school_trip assigns students to taxis in order

# filling each taxi with up to 4 students for example

def school_trip(n):
    if n <= 0:
        return []
    taxis = []
    taxi_number = 1
    remaining = n
    while remaining > 0:                  # The function uses a while loop to continue assigning students to taxis until there are no students left (remaining > 0). Inside the loop, it calculates how many students can fit in the current taxi (up to 4) and updates the remaining number of students accordingly. Each taxi is labeled with its number and the number of students assigned to it, and this information is stored in the taxis list, which is returned at the end.
        # fill each taxi with up to 4 students
        students = min(4, remaining)
        taxis.append((f"taxi {taxi_number}:", students))
        remaining -= students
        taxi_number += 1
    return taxis


# simple checks to verify the functions
print("distribute_n(10, 3) =", distribute_n(10, 3))
print("pie_chart([50, 30, 20]) =", pie_chart([50, 30, 20]))
print("school_trip(10) =", school_trip(10))
