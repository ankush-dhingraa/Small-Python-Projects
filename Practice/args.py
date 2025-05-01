def add(*args):
    sum_of_args = 0
    for i in args:
        sum_of_args += i

    return sum_of_args

print(add(1,2,5))