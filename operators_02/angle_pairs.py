# Complete the function named angle_pairs that accepts three angles (integers), measured in degrees, as parameters
# It returns whether or not there exists both complementary and supplementary angles amongst the three angles passed
# for more info on this quiz, go to this url: http://www.programmr.com/anglepairs


def angle_pairs(x, y, z):
    if x + y == 90 or x + z == 90 or y + z == 90 or x + y == 180 or x + z == 180 or y + z == 180:
        return True
    else:
        return False


if __name__ == __main__:
    angle_pairs(30, 40, 20)
