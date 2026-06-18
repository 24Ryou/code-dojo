# https://www.codewars.com/kata/546f922b54af40e1e90001da
# --------------------------------- SOLUTION --------------------------------- #
def alphabet_position(text):
    # ord(letter) - 96
    return " ".join(str(ord(c.lower()) - 96) for c in text if c.isalpha())


print(alphabet_position("The sunset sets at twelve o' clock."))

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
