# If a four digit number is entered through the keyboard ,
# write a program to print a new number by adding one to each of its digits
# for more info on this quiz, go to this url: http://www.programmr.com/increase-digits-number-one


def increase_digits_of_a_number_by_one(number):
    numb_lst = map(int, list(str(number)))
    new_lst = []
    for i in numb_lst:
        new_lst.append(i + 1)
    return "".join(map(str, new_lst))


print(increase_digits_of_a_number_by_one(7896))
