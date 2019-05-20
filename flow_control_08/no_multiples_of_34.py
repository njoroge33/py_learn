# Write a function that takes a number and returns a list of integers from 0 to that number
# excluding multiples of 3 and 4
# for more info on this quiz, go to this url: http://www.programmr.com/no-multiples-34-0


def remove_mult_of_3_and_4(num):
    lst = [0]
    try:
        for i in range(0, num + 1):
            if i % 3 != 0 and i % 4 != 0:
                lst.append(i)
        return lst
    except TypeError:
        return "Wrong data type!: num expected as an integer"


if __name__ == "__main__":
    print(remove_mult_of_3_and_4(10))
