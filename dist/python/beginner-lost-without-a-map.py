# https://www.codewars.com/kata/57f781872e3d8ca2a000007e
# --------------------------------- SOLUTION --------------------------------- #
def maps(a):
    return [x*2 for x in a]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
test.assert_equals(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])
test.assert_equals(maps([]), [])