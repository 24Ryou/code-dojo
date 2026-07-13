# https://www.codewars.com/kata/59441520102eaa25260000bf
# --------------------------------- SOLUTION --------------------------------- #
def unusual_five():
    return ord('I')%ord('D')
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(unusual_five(), 5)