# https://www.codewars.com/kata/546e2562b03326a88e000020
# --------------------------------- SOLUTION --------------------------------- #
def square_digits(num):
    return int("".join([*map(lambda x: str(int(x) ** 2), str(num))]))
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(square_digits(9119), 811181)
test.assert_equals(square_digits(0), 0)