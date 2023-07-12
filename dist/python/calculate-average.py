# https://www.codewars.com/kata/57a2013acf1fa5bfc4000921
# --------------------------------- SOLUTION --------------------------------- #
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_average([1, 2, 3]), 2, "Failed for [1, 2, 3]")
        test.assert_equals(find_average([]), 0, "Failed for []")
        test.assert_approx_equals(find_average([1, 2]), 1.5, margin=1e-3, message="Failed for [1, 2]")
        