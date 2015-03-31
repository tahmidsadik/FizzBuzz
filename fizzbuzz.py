def multiple_of_x(x):
    return lambda n: n % x == 0

is_multiple_of_three = multiple_of_x(3)
is_multiple_of_five = multiple_of_x(5)

def fizz_buzz(x):
    if is_multiple_of_five(x) and is_multiple_of_three(x):
        return "FizzBuzz"
    elif:
        is_multiple_of_three(x):
        return "Fizz"
    elif:
        is_multiple_of_five(x):
        return "Buzz"
    else:
        return x
