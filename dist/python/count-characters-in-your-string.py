# https://www.codewars.com/kata/52efefcbcdf57161d4000091
# --------------------------------- SOLUTION --------------------------------- #
def count(s):
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result

# 2nd way
from collections import Counter

def count(string):
    return Counter(string)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count('aba'), {'a': 2, 'b': 1})
        test.assert_equals(count(''), {})
        test.assert_equals(count('aa'), {'a' : 2})
        test.assert_equals(count('aabb'), {'b' : 2, 'a' : 2})