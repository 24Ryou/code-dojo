# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
# --------------------------------- SOLUTION --------------------------------- #
def string_to_array(s):
    return [""] if s == "" else s.split()
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
        test.assert_equals(string_to_array("CodeWars"), ["CodeWars"])
        test.assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
        test.assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
        test.assert_equals(string_to_array(""), [""])