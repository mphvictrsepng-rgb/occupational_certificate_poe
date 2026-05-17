# Question 1: Discount Calculator

def discount_calculator():
    print("Question 1: Discount Calculator")
    original_price = float(input("Enter the original price: ").strip())              # original price. and I also added strip() to remove any extra spaces from the user input
    discount_percentage = float(input("Enter the discount percentage: ").strip())    # discount percent

    discount_amount = original_price * discount_percentage / 100                # amount saved
    final_price = original_price - discount_amount                            # final price

    print(f"Discount amount: R{discount_amount:.2f}")
    print(f"Final price after discount: R{final_price:.2f}")
    print()


# Question 2: Exam Percentage and Grade 

def exam_percentage_and_grade():
    print("Question 2: Exam Percentage and Grade")
    marks_obtained = float(input("Enter marks obtained: ").strip())        # marks obtained
    total_marks = float(input("Enter total marks: ").strip())                # total marks

    if total_marks <= 0:
        print("Total marks must be greater than zero.")                 # invalid total
    else:
        percentage = marks_obtained / total_marks * 100               # calc percentage
        print(f"Percentage: {percentage:.2f}%")

        if percentage >= 75:
            grade = "Distinction"
        elif percentage >= 60:
            grade = "Merit"
        elif percentage >= 50:
            grade = "Pass"
        else:
            grade = "Fail"

        print(f"Grade: {grade}")
    print()


# Question 3: Salary Increase

def salary_increase():
    print("Question 3: Salary Increase")
    current_salary = float(input("Enter current salary: ").strip())  # current salary
    increase_percentage = float(input("Enter percentage increase: ").strip())  # increase percent

    increase_amount = current_salary * increase_percentage / 100  # raise amount
    new_salary = current_salary + increase_amount  # new salary

    print(f"Increase amount: R{increase_amount:.2f}")
    print(f"New salary after increase: R{new_salary:.2f}")
    print()


# Question 4: Profit Percentage

def profit_percentage():
    print("Question 4: Profit Percentage")
    cost_price = float(input("Enter cost price: ").strip())               # cost price
    selling_price = float(input("Enter selling price: ").strip())         # selling price

    profit_or_loss = selling_price - cost_price                           # profit/loss amount
    if cost_price == 0:
        print("Cost price must be greater than zero to calculate profit percentage.")
    else:
        percentage = profit_or_loss / cost_price * 100                      # profit %
        result = "profit" if profit_or_loss > 0 else "loss" if profit_or_loss < 0 else "no profit or loss"     # i wrote this to determine if it's a profit, loss, or break-even situation based on the value of profit/loss. chose to i chose to use a ternary operator for cleaner code and to avoid multiple if-else statements, but i'm not sure if it's the best choice for readability tho 

        print(f"{result.capitalize()}: R{abs(profit_or_loss):.2f}")       #abs to get the absolute value of profit/loss, and capitalize() to make the first letter uppercase for better presentation
        if result != "no profit or loss":
            print(f"{result.capitalize()} percentage: {abs(percentage):.2f}%")   
    print()


if __name__ == "__main__":                     # this is the main function to run all the questions
    discount_calculator()
    exam_percentage_and_grade()
    salary_increase()
    profit_percentage()