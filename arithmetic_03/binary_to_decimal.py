# Write a simple program convert integer in base 2(binary) to base 10(Decimal) 
# for more info on this quiz, go to this url: http://www.programmr.com/binary-decimal-1


def binary_decimal(base_2):
    numb = str(base_2)
    return int(numb, 2)


if __name__ == "__main__":
    print(binary_decimal(1101))
