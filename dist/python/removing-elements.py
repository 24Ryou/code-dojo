# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
# --------------------------------- SOLUTION --------------------------------- #
def remove_every_other(my_list):
    return my_list[::2]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                   ['Hello', 'Hello Again'])
test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                   [1, 3, 5, 7, 9])
test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                   [['Goodbye']])

