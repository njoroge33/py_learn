# Write a Python program to allow the user to input temperature in Celsius and convert it into Fahrenheit 
# (Consider only two digits after the decimal in the result) 
# The formula is:Fahrenheit = (9 
# 0/5 
# 0) x Celsius + 32 
# for more info on this quiz, go to this url: http://www.programmr.com/celsius-fahrenheit-converter


def celsius_fahrenheit(celsius):
    fahrenheit = (9.0/5.0 * celsius + 32)
    print(f"{celsius} degree celsius is equal to {fahrenheit} fahrenheit")
    return fahrenheit


if __name__ == "__main__":
    celsius_fahrenheit(20)
