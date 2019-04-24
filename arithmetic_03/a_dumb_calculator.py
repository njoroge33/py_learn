# Make a simple numeric calculator
# It should prompt the user for three numbers
# Then add the numbers together and divide by 2
# Display the result
# Your program must support numbers with decimals and not just integers
# for more info on this quiz, go to this url: http://www.programmr.com/dumb-calculator-3


def calculator(a, b, c):
    total = float((a + b + c)/2)
    return round(total, 2)


if __name__ == "__main__":
    print(calculator(4.2, 5, 8.6))
