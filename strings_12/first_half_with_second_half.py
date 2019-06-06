# Given a string from user, swap the first half with second half.If the string length is odd,
# take the lower first half and swap. And if the string length is 1, leave it alone.
# Input any String:abcde 
# Output:cdeab
# for more info on this quiz, go to this url: http://www.programmr.com/first-half-second-half-1


def swap_char(x_str):
    a = (len(x_str))//2
    y_str = x_str[a::] + x_str[:a]
    return y_str


if __name__ == "__main__":
    print(swap_char("abcde"))
