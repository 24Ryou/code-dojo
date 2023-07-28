# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# --------------------------------- SOLUTION --------------------------------- #
def sort_array(numbers : list):
    odds = filter(lambda x:x & 1 == 1 , numbers)
    odds = sorted(odds , reverse=True)
    for ndx , item in enumerate(numbers):
        if item & 1 == 1:
            numbers[ndx] = odds.pop()
    return numbers
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
test.assert_equals(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
test.assert_equals(sort_array([]),[])