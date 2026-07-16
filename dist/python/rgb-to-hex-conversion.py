# https://www.codewars.com/kata/513e08acc600c94f01000001
# --------------------------------- SOLUTION --------------------------------- #
def rgb(r, g, b):
    return ''.join(f"{max(0, min(_, 255)):02X}" for _ in [r,g,b])
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
        test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
        test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")