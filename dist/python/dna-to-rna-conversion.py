# https://www.codewars.com/kata/5556282156230d0e5e000089
# -------------------------------- SOLUTION ------------------------------- #
def dna_to_rna(dna : str):
    table = str.maketrans("GCAT" , "GCAU")
    return dna.translate(table)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Sample Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(dna_to_rna("TTTT"), "UUUU")
        test.assert_equals(dna_to_rna("GCAT"), "GCAU")
        test.assert_equals(dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")