# https://www.codewars.com/kata/539ee3b6757843632d00026b
# --------------------------------- SOLUTION --------------------------------- #
def capitals(word):
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []
    for i in range(len(word)):
        if word[i] in caps:
            res.append(i)
    return res

# 2nd way
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals( capitals('CodEWaRs'), [0,3,4,6] )