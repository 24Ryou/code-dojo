# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# --------------------------------- SOLUTION --------------------------------- #
def find_uniq(arr):
    arr = sorted(arr)
    return arr[0] if arr[0] != arr[1] else arr[-1]

# 2nd way
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)