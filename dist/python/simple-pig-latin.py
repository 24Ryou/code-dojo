# https://www.codewars.com/kata/520b9d2ad5c005041100000f
# --------------------------------- SOLUTION --------------------------------- #
def pig_it(text):
    words = [w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split()]
    return ' '.join(words)

# 2nd way
def pig_it(text):
    return " ".join(
        w[1:] + w[0] + "ay" if w.isalpha() else w
        for w in text.split()
    )

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(pig_it('This is my string !'))
# hisTay siay ymay tringsay