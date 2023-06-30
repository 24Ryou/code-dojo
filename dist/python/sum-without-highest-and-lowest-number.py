# 576b93db1129fcf2200001e6
# -------------------------------- SOLUTION ------------------------------- #
def sum_array(arr):
    if not arr:
        return 0
    arr.sort()
    return sum(arr[1:-1])
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('None or Empty')
    def basic_test_cases():
        test.assert_equals(sum_array(None), 0)
        test.assert_equals(sum_array([]), 0)

    @test.it("Only one Element")
    def one_test_cases():
        test.assert_equals(sum_array([3]), 0)
        test.assert_equals(sum_array([-3]), 0)
        
    @test.it("Only two Element")
    def two_test_cases():
        test.assert_equals(sum_array([ 3, 5]), 0)
        test.assert_equals(sum_array([-3, -5]), 0)

    @test.it("Real Tests")
    def real_test_cases():
        test.assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
        test.assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
        test.assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
        test.assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)