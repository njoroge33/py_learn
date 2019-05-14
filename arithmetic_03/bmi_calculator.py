# The body mass index (BMI) is commonly used by health and nutrition professionals to estimate human body fat
# in populations
# It is computed by taking the individual's weight (mass) in kilograms and dividing it
#  by the square of their height in meters
# Round off the the result to two decimal places
# for more info on this quiz, go to this url: http://www.programmr.com/bmi-calculator-4


def bmi_calculator(weight, height):
    return round(weight/(height**2), 2)


if __name__ == "__main__":
    print(bmi_calculator(45, 1.5))
