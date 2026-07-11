# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b
# --------------------------------- SOLUTION --------------------------------- #
def human_years_cat_years_dog_years(human_years):
    catyear, dogyear = (15,15) if human_years < 2 else (24 + ((human_years-2) * 4), 24 + ((human_years -2)* 5))
    return [human_years, catyear, dogyear]

# 2nd way
def human_years_cat_years_dog_years(human_years):
    cat = 15 if human_years == 1 else 24 + (human_years - 2) * 4
    dog = 15 if human_years == 1 else 24 + (human_years - 2) * 5
    return [human_years, cat, dog]

# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("one")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(1), [1,15,15])
    @test.it("two")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(2), [2,24,24])
    @test.it("ten")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(10), [10,56,64])