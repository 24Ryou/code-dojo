# https://www.codewars.com/kata/55cbc3586671f6aa070000fb
# --------------------------------- SOLUTION --------------------------------- #
def check_for_factor(base, factor):
    # your code here
    if base % factor == 0:
        return True
    else:
        return False
    
def check_for_factor(base, factor):
    return base % factor == 0

# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():    
    @test.it("Should return True")
    def should_return_true():
        test.assert_equals(check_for_factor(10, 2), True)
        test.assert_equals(check_for_factor(63, 7), True)
        test.assert_equals(check_for_factor(2450, 5), True)
        test.assert_equals(check_for_factor(24612, 3), True)
        
    @test.it("Should return False")
    def should_return_false():
        test.assert_equals(check_for_factor(9, 2), False)
        test.assert_equals(check_for_factor(653, 7), False)
        test.assert_equals(check_for_factor(2453, 5), False)
        test.assert_equals(check_for_factor(24617, 3), False)