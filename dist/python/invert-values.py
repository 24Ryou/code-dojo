# https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
# --------------------------------- SOLUTION --------------------------------- #
def invert(lst):
    return [-x for x in lst]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Invert values")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        test.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
        test.assert_equals(invert([]), [])