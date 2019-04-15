# Write a program that takes a number as input and prints it, dropping any decimal places 
# for more info on this quiz, go to this url: http://www.programmr.com/drop-decimal


def drop_decimals():
    decimal = float(input("Please,Enter a number with a decimal place: "))
    number = int(decimal)
    return number


print(drop_decimals())
