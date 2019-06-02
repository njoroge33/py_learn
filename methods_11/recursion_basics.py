# Write a method 'fibo()' which accepts a single integer x as argument 
# Return the fibonacci series till x numbers recursively from that function 
# for more info on this quiz, go to this url: http://www.programmr.com/recursion-basics-1


def fibo(int_x):
    if int_x < 2:
        return int_x
    return fibo(int_x - 1) + fibo(int_x - 2)


print(fibo(9))
