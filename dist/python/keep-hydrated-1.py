# https://www.codewars.com/kata/582cb0224e56e068d800003c
# --------------------------------- SOLUTION --------------------------------- #
def litres(time):
    return int(time * 0.5)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(litres(2), 1, 'should return 1 litre')
        test.assert_equals(litres(1.4), 0, 'should return 0 litres')
        test.assert_equals(litres(12.3), 6, 'should return 6 litres')
        test.assert_equals(litres(0.82), 0, 'should return 0 litres')
        test.assert_equals(litres(11.8), 5, 'should return 5 litres')
        test.assert_equals(litres(1787), 893, 'should return 893 litres')
        test.assert_equals(litres(0), 0, 'should return 0 litres')