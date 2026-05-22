# 1.4 
def get_row_colour(index):
    colours = ["red", "green", "blue"]
    return colours[index % 3]


# to se if it works nicely
print(get_row_colour(0))  # red
print(get_row_colour(1))  # green
print(get_row_colour(2))  # blue