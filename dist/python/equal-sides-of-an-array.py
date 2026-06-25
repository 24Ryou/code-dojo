# https://www.codewars.com/kata/5679aa472b8f57fb8c000047
# --------------------------------- SOLUTION --------------------------------- #
def find_even_index(arr):
    for ndx in range(0, len(arr)):
        left = sum(x for x in arr[:ndx+1])
        right = sum(x for x in arr[ndx:])
        if  left == right :
            return ndx 
    return -1

# 2nd way
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
# ----------------------------------- TEST ----------------------------------- #
find_even_index([1,2,3,4,3,2,1])
find_even_index([1,100,50,-51,1,1])
# import codewars_test as test
