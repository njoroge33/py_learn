# You have a red lottery ticket showing ints a, b, and c, each of which is 0, 1, or 2.
# If they are all the value 2, the result is 10.
# Otherwise if they are all the same, the result is 5.
# Otherwise so long as both b and c are different from a, the result is 1.
# Otherwise the result is 0.
# Write a function that given a, b, c, returns the value of the ticket
# for more info on this quiz, go to this url: http://www.programmr.com/red-lottery-ticket-3


def find_ticket_value(a, b, c):
    try:
        if a == 2 and b == 2 and c == 2:
            return 10
        elif a == b and b == c and a == c:
            return 5
        elif b != a and c != a:
            return 1
        else:
            return 0
    except TypeError:
        return "wrong Data Type!"


if __name__ == "__main__":
    print(find_ticket_value(0, 2, 2))
