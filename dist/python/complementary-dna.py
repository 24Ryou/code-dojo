# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
# --------------------------------- SOLUTION --------------------------------- #
def DNA_strand(dna):
    # code here
    s = str.maketrans('ATCG', 'TAGC')
    return dna.translate(s)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():     
        test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
        test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
        test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")