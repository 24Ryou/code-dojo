# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
# --------------------------------- SOLUTION --------------------------------- #
def reverse_words(text):
    txt_list = [x[::-1] for x in text.split(' ')]
    return ' '.join(txt_list)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

@test.describe("Sample Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'), 'ehT kciuq nworb xof spmuj revo eht yzal .god', "Input: 'The quick brown fox jumps over the lazy dog.'")
        test.assert_equals(reverse_words('apple'), 'elppa', "Input: 'apple'")
        test.assert_equals(reverse_words('a b c d'), 'a b c d', "Input: 'a b c d'")
        test.assert_equals(reverse_words('  double  spaced  words  '), '  elbuod  decaps  sdrow  ', "Input: '  double  spaced  words  '")

#----------
text = "  This  is  an example   string  "
print(text.split())  # Default split
## output ['This', 'is', 'an', 'example', 'string']
print(text.split(' '))
## output ['', '', 'This', '', 'is', '', 'an', 'example', '', '', 'string', '', '']