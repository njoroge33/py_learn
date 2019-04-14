# Make a simple numeric calculator 
# It should prompt the user for three numbers 
# Then add the numbers together and divide by 2 
# Display the result 
# Your program must support numbers with decimals and not just integers 
# for more info on this quiz, go to this url: http://www.programmr.com/dumb-calculator-5


def simple_calc():
    numbers = input("Enter three numbers separated with a space: ")
    lst = numbers.split()
    total = 0
    for i in lst:
        total += int(i)
    return total


print(simple_calc())
