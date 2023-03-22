

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def lucas(num):
    if num == 0:
        return 2
    elif num == 1:
        return 1
    return lucas(num - 1) + lucas(num - 2)


def sum_series(num, first, second):
    if num == 0:
        return first
    elif num == 1:
        return second
    else:
        return sum_series(num - 1, first, second) + sum_series(num - 2, first, second)


sum_series(7, 3, 2)
