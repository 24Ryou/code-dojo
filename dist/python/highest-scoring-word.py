# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
# --------------------------------- SOLUTION --------------------------------- #
def high(x):
    words = x.split()
    max_counted = 0
    for word in words:
        count = 0
        for ch in word:
            count += ord(ch) - 96
        if count > max_counted:
            max_counted = count
            _ = word
    return _
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
test.assert_equals(high('aa b'), 'aa')
test.assert_equals(high('b aa'), 'b')
test.assert_equals(high('bb d'), 'bb')
test.assert_equals(high('d bb'), 'd')
test.assert_equals(high("aaa b"), "aaa")