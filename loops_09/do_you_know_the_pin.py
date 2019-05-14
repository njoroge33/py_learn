# You have to design the code such that the user has only three tries to guess the correct pin of the account 
# for more info on this quiz, go to this url: http://www.programmr.com/do-you-know-pin-2


class LengthError(Exception):
    pass


def user():
    num = 4942
    tries = 0
    try:
        while tries < 3:
            a = int(input("Enter your pin: "))

            tries += 1
            if len(str(a)) != 4:
                raise LengthError('Pin length should be four!')
            if a != num:
                print("try again!")
            elif a == num:
                break
        else:
            return "You are out of tries!"
    except ValueError:
        return "ValueError:Pin expected as integer!"


print(user())
