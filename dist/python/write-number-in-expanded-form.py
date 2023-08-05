# https://www.codewars.com/kata/5842df8ccbd22792a4000245
# --------------------------------- SOLUTION --------------------------------- #
def expanded_form(number):
    nums = list()
    place_value = 1
    while number > 0:
        digit = number % 10
        if digit != 0:
            nums.append(str(digit * place_value))
        number //= 10
        place_value *= 10
    nums.reverse()
    return " + ".join(nums)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Sample tests")
def sample_tests():
    
    @test.it("Should pass sample tests")
    def should_pass_sample_tests():
        test.assert_equals(expanded_form(12), '10 + 2');
        test.assert_equals(expanded_form(42), '40 + 2');
        test.assert_equals(expanded_form(70304), '70000 + 300 + 4');