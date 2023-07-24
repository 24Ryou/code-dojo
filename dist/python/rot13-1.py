# https://www.codewars.com/kata/530e15517bc88ac656000716
# --------------------------------- SOLUTION --------------------------------- #
def rot13(message):
   rot13_table = str.maketrans(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
    'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    )
   return message.translate(rot13_table)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed tests")
def tests():
        
    @test.it("Should obtain correct Rot13 encoding on fixed strings")
    def test_rot13_fixed_strings():
        test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')