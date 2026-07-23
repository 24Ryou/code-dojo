# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed
# --------------------------------- SOLUTION --------------------------------- #
def replace_exclamation(st):
    return ''.join('!' if x in 'aeiouAEIOU' else x for x in st)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(replace_exclamation("Hi!") , "H!!")
        test.assert_equals(replace_exclamation("!Hi! Hi!") , "!H!! H!!")
        test.assert_equals(replace_exclamation("aeiou") , "!!!!!")
        test.assert_equals(replace_exclamation("ABCDE") , "!BCD!")