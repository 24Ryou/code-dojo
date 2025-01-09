# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e
# --------------------------------- SOLUTION --------------------------------- #
def repeat_str(repeat, string):
    return repeat * string
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(repeat_str(4, 'a'), 'aaaa')
        test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
        test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
    