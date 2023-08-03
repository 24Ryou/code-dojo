# https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# --------------------------------- SOLUTION --------------------------------- #
import string
def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    sentence = "".join([chr for chr in sentence.lower() if chr.isalpha()])
    return set(alphabet) == set(sentence)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)