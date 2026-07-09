# https://www.codewars.com/kata/55983863da40caa2c900004e
# --------------------------------- SOLUTION --------------------------------- #
def next_bigger(n):
    digits = list(str(n))

    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            for j in range(len(digits) - 1, i, -1):
                if digits[j] > digits[i]:
                    digits[i], digits[j] = digits[j], digits[i]
                    digits[i + 1:] = sorted(digits[i + 1:])
                    return int(''.join(digits))
    return -1


# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

test.assert_equals(next_bigger(12),   21)
test.assert_equals(next_bigger(21),   -1)
test.assert_equals(next_bigger(513),  531)
test.assert_equals(next_bigger(2017), 2071)
test.assert_equals(next_bigger(414),  441)
test.assert_equals(next_bigger(144),  414)
