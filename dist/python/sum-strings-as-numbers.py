# https://www.codewars.com/kata/5324945e2ece5e1f32000370
# --------------------------------- SOLUTION --------------------------------- #
def sum_strings(x, y):
    x = x.lstrip('0') or '0'
    y = y.lstrip('0') or '0'

    if len(x) > len(y):
        y = y.zfill(len(x))
    elif len(y) > len(x):
        x = x.zfill(len(y))

    carry = 0
    result = []

    for i in range(len(x) - 1, -1, -1):
        num_x = int(x[i])
        num_y = int(y[i])

        total = num_x + num_y + carry
        result.append(str(total % 10))
        carry = total // 10

    if carry:
        result.append(str(carry))

    return ''.join(reversed(result))

# 2nd way
def sum_strings(x, y):
    l = max(len(x), len(y))
    x, y = x.zfill(l), y.zfill(l)
    
    res = []
    carry = 0

    for i in range(l - 1, -1, -1):
        carry, d = divmod(int(x[i]) + int(y[i]) + carry, 10)
        res.append(str(d))

    if carry:
        res.append("1")

    return ''.join(reversed(res)).lstrip('0') or '0'

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(sum_strings('010', '30'))
# print(sum_strings('999', '1'))
# print(9//10, 12%10)
