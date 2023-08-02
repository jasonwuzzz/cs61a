# Qustion 1.1
def keep_ints(cond, n):
    for i in range(1, n + 1):
        if cond(i):
            print(i)

# Question 1.2
def make_keeper(n):
    def func(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    return func

# Question 1.4
lambda_func = lambda h: lambda x: lambda y: h(x, y)
make_adder = lambda_func(lambda x, y: x + y)
add_three = make_adder(3)
add_three(2)

# Question 1.7
def print_delayed(x):
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# Question 1.8
def print_n(n):
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print
