# Write a program to swap the values of two variables 
# for more info on this quiz, go to this url: http://www.programmr.com/swap-values-two-variable-1


def swap_variables():
    x = input("Enter value of X: ")
    y = input("Enter value of Y: ")
    a = x
    x = y
    y = a
    print(f"After swapping, The value of X is, {x}, while value of Y is, {y},")
    return x, y


print(swap_variables())
