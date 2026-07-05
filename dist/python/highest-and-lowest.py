# https://www.codewars.com/kata/554b4ac871d6813a03000035
# --------------------------------- SOLUTION --------------------------------- #
def high_and_low(numbers):
    high = '-9000'
    low = '9000'
    for num in numbers.split():
        if int(num) > int(high):
            high = num
        if int(num) < int(low):
            low = num
    return high + ' ' + low

# 2nd way - better
def high_and_low(numbers):
    nums = list(map(int, numbers.split()))
    return f"{max(nums)} {min(nums)}"
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) # "42 -9"