# Ask the user to enter two variables 'a' and 'b' 
# Then assign the value of 'b-a +100' to 'b' and print values of both 'a' and 'b' as shown below 
# for more info on this quiz, go to this url: http://www.programmr.com/test-your-variable-knowledge


def assign_variables():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    total = b - a + 100
    return total


print(assign_variables())
