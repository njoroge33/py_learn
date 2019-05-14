# Write a Python program to multiply two numbers entered by the user and display their product 
# for more info on this quiz, go to this url: http://www.programmr.com/multiply-two-numbers-1


def multiply_number():
    print("Please enter two numbers")
    user_inputs = []
    result = 1
    for i in range(2):
        user_input = int(input("Enter a number: "))
        user_inputs.append(user_input)
    for i in user_inputs:
        result = i * result
    return result


print(multiply_number())
