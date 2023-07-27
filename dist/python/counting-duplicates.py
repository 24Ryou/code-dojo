# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# --------------------------------- SOLUTION --------------------------------- #
def duplicate_count(text):
    dic = {}
    for char in text.lower():
        dic[char] = dic.get(char , 0) + 1
    c = 0
    for key in dic:
        if dic[key] > 1:
            c += 1
    return c
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)