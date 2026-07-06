# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
# --------------------------------- SOLUTION --------------------------------- #
def find_short(s):
    return min(len(x) for x in s.split())
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(find_short("bitcoin take over the world maybe who knows perhaps")) # 3