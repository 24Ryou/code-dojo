# https://www.codewars.com/kata/52449b062fb80683ec000024
# --------------------------------- SOLUTION --------------------------------- #
def generate_hashtag(s):
    res = ''
    if s == '':
        return False
    words = s.lower().split()
    res =  '#' + ''.join(x[0].upper() + x[1:] for x in words)
    return False if len(res) > 140 else res

# 2nd way
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output

# 3rd way - best way
def generate_hashtag(s):
    words = s.split()
    if not words:
        return False

    tag = "#" + "".join(w.capitalize() for w in words)
    return tag if len(tag) <= 140 else False

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(generate_hashtag('CoDeWaRs is niCe'))
