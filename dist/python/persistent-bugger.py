# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
# --------------------------------- SOLUTION --------------------------------- #
def persistence(n, times = 0):
    if n < 10:
        return times
    m = 1
    while n > 0:
        m *= n % 10
        n //= 10
    return persistence(m, times + 1)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Persistent Bugger.")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(persistence(39), 3)
        test.assert_equals(persistence(4), 0)
        test.assert_equals(persistence(25), 2)
        test.assert_equals(persistence(999), 4)
