# https://www.codewars.com/kata/602db3215c22df000e8544f0
# --------------------------------- SOLUTION --------------------------------- #
def two_are_positive(a, b, c):
    count = bool(a > 0 ) + bool(b > 0) + bool(c > 0)
    return count == 2
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.it("Example Tests")
def example_tests():
    test.assert_equals(two_are_positive(2, 4, -3), True)
    test.assert_equals(two_are_positive(-4, 6, 8), True)
    test.assert_equals(two_are_positive(4, -6, 9), True)
    test.assert_equals(two_are_positive(-4, 6, 0), False)
    test.assert_equals(two_are_positive(4, 6, 10), False)
    test.assert_equals(two_are_positive(-14, -3, -4), False)