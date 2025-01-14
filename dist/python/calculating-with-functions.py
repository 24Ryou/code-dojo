# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
# --------------------------------- SOLUTION --------------------------------- #
def zero(op=None):  return 0 if not op else op(0)
def one(op=None):   return 1 if not op else op(1)
def two(op=None):   return 2 if not op else op(2)
def three(op=None): return 3 if not op else op(3)
def four(op=None):  return 4 if not op else op(4)
def five(op=None):  return 5 if not op else op(5)
def six(op=None):   return 6 if not op else op(6)
def seven(op=None): return 7 if not op else op(7)
def eight(op=None): return 8 if not op else op(8)
def nine(op=None):  return 9 if not op else op(9)

def plus(y):        return lambda x : x + y
def minus(y):       return lambda x : x - y
def times(y):       return lambda x : x * y
def divided_by(y):  return lambda x : x // y
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(seven(times(five())), 35)
        test.assert_equals(four(plus(nine())), 13)
        test.assert_equals(eight(minus(three())), 5)
        test.assert_equals(six(divided_by(two())), 3)