import math                  #I imported the math module to use mathematical functions like sqrt for calculating square roots.

# 1.1 - Using Pythagorean theorem: c² = a² + b²
a = 3
b = 4
hypotenuse = math.sqrt(a**2 + b**2)
print(f"1.1 - Hypotenuse: {hypotenuse} cm")

# 1.2 - Distance between two points using the distance formula
# distance = sqrt((x2-x1)² + (y2-y1)²)
x1, y1 = 4, 5            #Coordinates of point A
x2, y2 = 6, 7             #Coordinates of point B
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"1.2 - Distance between A and B: {distance:.2f} units")

# 1.3 - For 4D space, the distance formula extends the pattern
# distance = sqrt((x2-x1)² + (y2-y1)² + (z2-z1)² + (w2-w1)²)
formula_4d = "sqrt((x2-x1)² + (y2-y1)² + (z2-z1)² + (w2-w1)²)"
print(f"1.3 - 4D distance formula: {formula_4d}")
