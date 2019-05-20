# Write a program that receives two numbers and then performs a logical XOR operation on them 
# for more info on this quiz, go to this url: http://www.programmr.com/logical-xor-0


def logical_xor(a, b):
    return bin(a ^ b)


if __name__ == "__main__":
    print(logical_xor(14, 5))
