# https://www.codewars.com/kata/55b42574ff091733d900002f
# --------------------------------- SOLUTION --------------------------------- #
def friend(list_):
    return [x for x in list_ if len(x) == 4]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
        test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
        test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])