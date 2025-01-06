# https://www.codewars.com/kata/57eaeb9578748ff92a000009
# --------------------------------- SOLUTION --------------------------------- #
def sum_mix(arr):
    #your code here
    res = 0
    for i in arr:
        res = res + int(i)
            
    return res
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test