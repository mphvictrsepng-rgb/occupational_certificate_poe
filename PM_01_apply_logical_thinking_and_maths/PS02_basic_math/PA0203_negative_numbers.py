# Question 1.1: Property with negative numbers

def question_1_1():
    print("Question 1.1: Assume that b > cd, if c is replaced with -c does the property still hold?")
    print("Answer: Yes, if b > cd, then b > -c*d is not necessarily true.")
    print("Example: Let b = 5, c = 2, d = 1")
    print("Original: 5 > 2*1 = 5 > 2 (True)")
    print("With -c: 5 > -2*1 = 5 > -2 (True)")
    print("But the comparison changes. The property doesn't hold in the same way.")
    print()


# Question 1.2: Example of d > e and -d < -e
def question_1_2():
    print("Question 1.2: Provide an example of d > e and -d < -e")
    d = 10                                                            # example value
    e = 3                                                           # example value
    print(f"Let d = {d} and e = {e}")
    print(f"Check: d > e? {d} > {e} = {d > e}")
    print(f"Check: -d < -e? -{d} < -{e} = {-d < -e}")
    print("This shows that when we negate both sides, the inequality reverses.")
    print()


# Question 1.3: Calculate -(8)^2

def question_1_3():
    print("Question 1.3: Calculate -(8)^2")
    result = -(8**2)                                        # negative of 8 squared
    print(f"-(8)^2 = -(64) = {result}")
    print("Note: The negative sign applies after squaring, not before.")
    print()


# Question 1.4: Square root of y = 5, find y

def question_1_4():
    print("Question 1.4: The square root(y) = 5, what is the value of y?")
    square_root_y = 5                                              # given. I wanted to shorten the variable name for better readability, but chose a descriptive name to avoid confusion         
    y = square_root_y ** 2                                         # solve for y
    print(f"If square_root(y) = {square_root_y}")
    print(f"Then y = {square_root_y}^2 = {y}")
    print()


# Question 1.5: Express a - (-b) without using "-"

def question_1_5():
    print("Question 1.5: Express a - (-b) without using the '-' symbol")
    a = 7                                                              # example value
    b = 3                                                         # example value
    result = a + b              # a - (-b) is same as a + b
    print(f"a - (-b) can be expressed as a + b")
    print(f"Example: {a} - (-{b}) = {a} + {b} = {result}")
    print()


if __name__ == "__main__":            # this is the main function to run all the questions
    question_1_1()
    question_1_2()
    question_1_3()
    question_1_4()
    question_1_5()
