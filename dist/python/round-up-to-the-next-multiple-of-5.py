# https://www.codewars.com/kata/55d1d6d5955ec6365400006d
# --------------------------------- SOLUTION --------------------------------- #
def round_to_next5(n):
    if n%5 == 0:
        return n
    return 5 * ((n//5) + 1)
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
