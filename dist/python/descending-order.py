# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
# --------------------------------- SOLUTION --------------------------------- #
def descending_order(num):
    return int("".join(sorted(str(num) , reverse=True)))
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(descending_order(0), 0)
        test.assert_equals(descending_order(15), 51)
        test.assert_equals(descending_order(123456789), 987654321)