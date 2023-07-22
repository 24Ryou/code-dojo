# https://www.codewars.com/kata/542c0f198e077084c0000c2e
# --------------------------------- SOLUTION --------------------------------- #
def divisors(n):
    counts = 1
    for i in range(1 , n):
        counts += n%i == 0
    return counts
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(divisors(1), 1) 
        test.assert_equals(divisors(4), 3)
        test.assert_equals(divisors(5), 2)
        test.assert_equals(divisors(12), 6)
        test.assert_equals(divisors(30), 8)
        test.assert_equals(divisors(4096), 13)