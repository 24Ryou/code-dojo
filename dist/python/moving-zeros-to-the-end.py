# https://www.codewars.com/kata/52597aa56021e91c93000cb0
# --------------------------------- SOLUTION --------------------------------- #
# def move_zeros(lst):
#     cnt = 0
#     out = []
#     for itm in lst:
#         if itm == 0:
#             cnt += 1
#         else:
#             out.append(itm)
#     out = out + [0] * cnt
#     return out

# def move_zeros(lst):
#     return [x for x in lst if x != 0] + [0] * lst.count(0)

def move_zeros(lst):
    # False (0) comes before True (1) in sorting order
    return sorted(lst, key=lambda x: x == 0 and x is not True)
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])) # [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]