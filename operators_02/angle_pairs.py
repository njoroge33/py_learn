# Complete the function named angle_pairs that accepts three angles (integers), measured in degrees, as parameters
# It returns whether or not there exists both complementary and supplementary angles amongst the three angles passed
# for more info on this quiz, go to this url: http://www.programmr.com/anglepairs


def angle_pairs(x, y, z):
    a = x + y
    b = x + z
    c = y + z

    if (a == 90 or b == 90 or c == 90) and (a == 180 or b == 180 or c == 180):
        return True
    else:
        return False


if __name__ == "__main__":
    print(angle_pairs(50, 40, 60))
