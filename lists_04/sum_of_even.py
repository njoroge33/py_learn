# The sum of even numbers is always even
# Let's prove it ! Write a program that takes a list of numbers, and returns the sum of its even numbers only
# If the list has no even numbers, return 0
# for more info on this quiz, go to this url: http://www.programmr.com/sum-even


def sum_even(arr_x):
    a = []
    for i in arr_x:
        if i % 2 == 0:
            a.append(i)
    return sum(a)


if __name__ == "__main__":
    print(sum_even([1, 2, 3, 4, 5, 6, 7]))
