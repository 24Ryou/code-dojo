# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
# --------------------------------- SOLUTION --------------------------------- #
def count_positives_sum_negatives(arr):
    if not arr:
        return []
        
    positive_count = sum(1 for x in arr if x > 0)
    negative_sum = sum(x for x in arr if x < 0)

    return [positive_count, negative_sum]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
        test.assert_equals(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
        test.assert_equals(count_positives_sum_negatives([1]),[1,0])
        test.assert_equals(count_positives_sum_negatives([-1]),[0,-1])
        test.assert_equals(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
        test.assert_equals(count_positives_sum_negatives([]),[])