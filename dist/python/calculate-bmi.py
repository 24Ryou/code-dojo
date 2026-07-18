# https://www.codewars.com/kata/57a429e253ba3381850000fb
# --------------------------------- SOLUTION --------------------------------- #
def bmi(weight, height):
    b = weight / height ** 2
    if b <= 18.5:
        return 'Underweight'
    elif b <= 25.0:
        return 'Normal'
    elif b <= 30.0:
        return 'Overweight'
    else:
        return 'Obese'
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(bmi(50, 1.80), "Underweight", "For weight = 50 and height = 1.80")
        test.assert_equals(bmi(80, 1.80), "Normal", "For weight = 80 and height = 1.80")
        test.assert_equals(bmi(90, 1.80), "Overweight", "For weight = 90 and height = 1.80")
        test.assert_equals(bmi(100, 1.80), "Obese", "For weight = 100 and height = 1.80")