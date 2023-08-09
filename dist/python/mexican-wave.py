# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
# --------------------------------- SOLUTION --------------------------------- #
def wave(people):
    result = list()
    for i in range(len(people)):
        if people[i].isalpha():
            result.append(people[:i] + people[i].upper() + people[i+1:])
    return result
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe('Testing')
def example_tests():
    @test.describe('Example tests')
    def example_tests():
        result = ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case1():
            test.assert_equals(wave("hello"), result)

        result = ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case2():
            test.assert_equals(wave("codewars"), result)

        result = []

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case3():
            test.assert_equals(wave(""), result)

        result = ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs",
                  "two wordS"]

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case4():
            test.assert_equals(wave("two words"), result)

        result = [" Gap ", " gAp ", " gaP "]

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case5():
            test.assert_equals(wave(" gap "), result)

        result = ["A       b    ", "a       B    "]

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case6():
            test.assert_equals(wave("a       b    "), result)

        result = ["This is a few words", "tHis is a few words", "thIs is a few words", "thiS is a few words",
                  "this Is a few words", "this iS a few words", "this is A few words", "this is a Few words",
                  "this is a fEw words", "this is a feW words", "this is a few Words", "this is a few wOrds",
                  "this is a few woRds", "this is a few worDs", "this is a few wordS"]

        @test.it("Should return: '[" + ", ".join(result) + "]'")
        def example_test_case7():
            test.assert_equals(wave("this is a few words"), result)
