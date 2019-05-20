# Make a simple numeric calculator 
# It should prompt the user for three numbers 
# Then add the numbers together and divide by 2 
# Display the result 
# Your program must support numbers with decimals and not just integers 
# for more info on this quiz, go to this url: http://www.programmr.com/dumb-calculator-5


def simple_calc():
    print("Enter three numbers")
    user_inputs = []
    for i in range(3):
        user_input = float(input("Enter a number: "))
        user_inputs.append(user_input)
    total = sum(user_inputs) / 2
    return total


print(simple_calc())
