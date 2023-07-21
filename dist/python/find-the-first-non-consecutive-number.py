# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
# --------------------------------- SOLUTION --------------------------------- #
def first_non_consecutive(arr):
    for i in range(len(arr)-1) :
        if arr[i+1] - arr[i] != 1 :
            return arr[i+1]
    return None
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(first_non_consecutive([1,2,3,4,6,7,8]), 6)
        test.assert_equals(first_non_consecutive([1,2,3,4,5,6,7,8]), None)
        test.assert_equals(first_non_consecutive([4,6,7,8,9,11]), 6)
        test.assert_equals(first_non_consecutive([4,5,6,7,8,9,11]), 11)
        test.assert_equals(first_non_consecutive([31,32]), None)
        test.assert_equals(first_non_consecutive([-3,-2,0,1]), 0)
        test.assert_equals(first_non_consecutive([-5,-4,-3,-1]), -1)