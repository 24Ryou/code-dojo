# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
# --------------------------------- SOLUTION --------------------------------- #
def is_square(n):    
    return pow(n,1/2)**2 == n

# 2nd way
import math

def is_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n

# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
test.assert_equals(is_square( 0), True, "0 is a square number (0 * 0)")
test.assert_equals(is_square( 3), False, "3 is not a square number")
test.assert_equals(is_square( 4), True, "4 is a square number (2 * 2)")
test.assert_equals(is_square(25), True, "25 is a square number (5 * 5)")
test.assert_equals(is_square(26), False, "26 is not a square number")