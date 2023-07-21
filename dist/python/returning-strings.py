# https://www.codewars.com/kata/55a70521798b14d4750000a4
# --------------------------------- SOLUTION --------------------------------- #
def greet(name):
    return "Hello, %s how are you doing today?" % name
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
        test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
