# Write a program to extract each digit from an int, in the reverse order.
# Enter a number:123
# Reverse of number:321
# for more info on this quiz, go to this url: http://www.programmr.com/extracting-digits-0


def reverse(num):
    old_lst = list(str(num))
    new_lst = []
    last = len(old_lst)-1
    for i in range(len(old_lst)):
        while last >= 0:
            new_lst.append(old_lst[last])
            last -= 1
    return "".join(new_lst)


if __name__ == "__main__":
    print(reverse(123))
