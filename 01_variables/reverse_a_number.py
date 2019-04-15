# Write a program to reverse the input number entered by the user 
# for more info on this quiz, go to this url: http://www.programmr.com/reverse-number-5


def reverse_number():
    print("PLEASE ENTER MORE THAN TWO NUMBERS")
    number_lst = []
    for i in range(4):
        number = input("Enter a number: ")
        number_lst.append(number)
    number_lst.reverse()
    return "".join(number_lst)


print(reverse_number())
