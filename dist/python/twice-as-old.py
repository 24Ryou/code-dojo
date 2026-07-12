# https://www.codewars.com/kata/5b853229cfde412a470000d0
# --------------------------------- SOLUTION --------------------------------- #
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(twice_as_old(36,7) , 22)
        test.assert_equals(twice_as_old(55,30) , 5)
        test.assert_equals(twice_as_old(42,21) , 0)
        test.assert_equals(twice_as_old(22,1) , 20)
        test.assert_equals(twice_as_old(29,0) , 29)