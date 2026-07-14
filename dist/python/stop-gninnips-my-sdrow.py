# https://www.codewars.com/kata/5264d2b162488dc400000001
# --------------------------------- SOLUTION --------------------------------- #
def spin_words(sentence):
    return ' '.join(x[::-1] if len(x) >= 5 else x for x in sentence.split())
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Stop gninnipS My sdroW!")
def fixed_tests():
    @test.it("Single word")
    def _():
        test.assert_equals(spin_words("Welcome"), "emocleW")
        test.assert_equals(spin_words("to"), "to")
        test.assert_equals(spin_words("CodeWars"), "sraWedoC")

    @test.it("Multiple words")
    def _():
        test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")