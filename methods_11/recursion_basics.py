# Write a method 'fibo()' which accepts a single integer x as argument 
# Return the fibonacci series till x numbers recursively from that function 
# for more info on this quiz, go to this url: http://www.programmr.com/recursion-basics-1


def fibo(int_x):
    if int_x < 2:
        return int_x
    return fibo(int_x - 1) + fibo(int_x - 2)


def gen_series(int_x):
    x_lst = []
    for i in range(int_x + 1):
        x_lst.append(fibo(i))
    return x_lst


print(gen_series(9))
