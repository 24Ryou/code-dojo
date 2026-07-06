# https://www.codewars.com/kata/56747fd5cb988479af000028
# --------------------------------- SOLUTION --------------------------------- #
def get_middle(s):
    mid = len(s) // 2
    return s[mid-1:mid+1] if len(s) % 2 == 0 else s[mid]
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(get_middle('testing')) # t
print(get_middle('middle')) # dd