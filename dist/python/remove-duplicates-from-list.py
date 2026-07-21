# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
# --------------------------------- SOLUTION --------------------------------- #
def distinct(seq):
    return list(dict.fromkeys(seq))

# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(distinct([1]), [1])
        test.assert_equals(distinct([1, 2]), [1, 2])
        test.assert_equals(distinct([1, 1, 2]), [1, 2])
        test.assert_equals(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        test.assert_equals(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])
        