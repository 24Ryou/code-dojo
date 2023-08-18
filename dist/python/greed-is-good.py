# https://www.codewars.com/kata/5270d0d18625160ada0000e4
# --------------------------------- SOLUTION --------------------------------- #
def score(dice):
    points = {
        '111': 1000, '222': 200, '333': 300, '444': 400, '555': 500, '666': 600,
        '1': 100, '5': 50
    }
    dict_dice = dict()
    for num in dice:
        dict_dice[num] = dict_dice.get(num, 0) + 1
    result = 0
    for key, value in dict_dice.items():
        if value >= 3:
            if key in [1, 5]:
                result += points[str(key) * 3] + points[str(key)] * (value % 3)
            else:
                result += points[str(key) * 3]
        elif value < 3 and key in [1, 5]:
            result += points[str(key)] * value
    return result
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

test.assert_equals(score([5, 1, 3, 4, 1]), 250)
test.assert_equals(score([1, 1, 1, 3, 1]), 1100)
test.assert_equals(score([2, 3, 4, 6, 2]), 0)
test.assert_equals(score([4, 4, 4, 3, 3]), 400)
test.assert_equals(score([2, 4, 4, 5, 4]), 450)
