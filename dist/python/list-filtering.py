# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
# --------------------------------- SOLUTION --------------------------------- #
def filter_list(l):
    return [x for x in l if isinstance(x,int)]
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(filter_list([1, 'a', 'b', 0, 15])) # [1,0,15]