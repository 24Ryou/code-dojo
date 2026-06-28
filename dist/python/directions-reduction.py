# https://www.codewars.com/kata/550f22f4d758534c1100025a
# --------------------------------- SOLUTION --------------------------------- #
def dir_reduc(arr):
    stack = []

    opposite = {
        'WEST': 'EAST',
        'EAST': 'WEST',
        'SOUTH': 'NORTH',
        'NORTH': 'SOUTH'
    }

    for d in arr:
        if stack and opposite[d] == stack[-1]:
            stack.pop()
        else:
            stack.append(d)

    return stack

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(dir_reduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"]))