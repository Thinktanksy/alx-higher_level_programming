#!/usr/bin/python3


if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""

    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    sum_result = add(a,b)
    diff_result = subtract(a,b)
    prod_result = multiply(a,b)
    quot_result = divide(a,b)

    print("The sum of {} and {} is {}".format(a, b, sum_result))
    print("The difference of {} and {} is {}".format(a, b, diff_result))
