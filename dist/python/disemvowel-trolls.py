# https://www.codewars.com/kata/52fba66badcd10859f00097e
# --------------------------------- SOLUTION --------------------------------- #
def disemvowel(string_):
    return ''.join(x for x in string_ if x not in 'aeiouAEIOU')
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(disemvowel("What are you, a communist?")) # Wht r y,  cmmnst?