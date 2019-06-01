# Write a function which receives a number as a parameter and
# returns True or False after checking if the number is Automorphic or not
# An automorphic number is a number whose square "ends" in the same digit as the number itself 
# for more info on this quiz, go to this url: http://www.programmr.com/automorphic-number-0

# created one that checks from 1-99


def auto_number(number):
    sq = number * number
    while number > 0:
        if len(list(map(int, str(number)))) == 1:
            if number % 10 != sq % 10:
                return False

            return True

        elif len(list(map(int, str(number)))) == 2:
            if number % 100 != sq % 100:
                return False

            return True
        else:
            break


if __name__ == "__main__":
    print(auto_number(99))
