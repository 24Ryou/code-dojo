# https://www.codewars.com/kata/586f6741c66d18c22800010a
# --------------------------------- SOLUTION --------------------------------- #
def sequence_sum(begin_number, end_number, step):
    return sum (x for x in range(begin_number, end_number+1, step))

print(sequence_sum(2,2,2))
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
