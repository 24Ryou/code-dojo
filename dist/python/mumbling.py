# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
# --------------------------------- SOLUTION --------------------------------- #
def accum(st):
    return '-'.join(((val*(ndx+1)).capitalize() for ndx, val in enumerate(st)))

# 2nd way
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# 3rd way - cleanest
def accum(s):
    parts = []
    for i, c in enumerate(s):
        parts.append(c.upper() + c.lower() * i)
    return '-'.join(parts)

# ----------------------------------- TEST ----------------------------------- #
print(accum('abcd'))
# import codewars_test as test
