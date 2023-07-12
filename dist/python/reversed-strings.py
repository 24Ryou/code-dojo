# https://www.codewars.com/kata/5168bb5dfe9a00b126000018
# --------------------------------- SOLUTION --------------------------------- #
def solution(string):
    return string[::-1]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.it('Basic Test Cases')
def basic_test_cases():
    test.assert_equals(solution('world'), 'dlrow')
    test.assert_equals(solution('hello'), 'olleh')
    test.assert_equals(solution(''), '')
    test.assert_equals(solution('h'), 'h')