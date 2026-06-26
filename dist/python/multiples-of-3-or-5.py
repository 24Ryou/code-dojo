# https://www.codewars.com/kata/514b92a657cdc65150000006
# --------------------------------- SOLUTION --------------------------------- #
def solution(number):
    nums = []
    condition1 = lambda x: x % 3 == 0
    condition2 = lambda x: x % 5 == 0
    if number <= 0: return 0
    for i in range(1, number):
        if condition1(i) or condition2(i):
            nums.append(i)
    return sum(nums)

# 2nd way
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# 3rd way - cleaner
def solution(number):
    if number <= 0:
        return 0
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# ----------------------------------- TEST ----------------------------------- #
print(solution(16)) # 23
# import codewars_test as test
