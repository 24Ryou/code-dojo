# https://www.codewars.com/kata/55a2d7ebe362935a210000b2
# --------------------------------- SOLUTION --------------------------------- #
def find_smallest_int(arr):
    return min(arr)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        test.assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        test.assert_equals(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)