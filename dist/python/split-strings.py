# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
# --------------------------------- SOLUTION --------------------------------- #
def solution(s):
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    if len(s) % 2 == 1:
        pairs[-1] += "_"
    return pairs
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)