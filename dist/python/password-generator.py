# https://www.codewars.com/kata/58ade2233c9736b01d0000b3
# --------------------------------- SOLUTION --------------------------------- #
import random
def password_gen():
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    all_chars = lowercase + uppercase + digits
    password_length = random.randint(3,17)
    password += random.choices(all_chars, k=password_length)

    return "".join(password)

'''
6 - 20 characters long
contains at least one lowercase letter
contains at least one uppercase letter
contains at least one number
contains only alphanumeric characters (no special characters)
'''

#--------------------
from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER, digits as DIGITS
from random import choice, shuffle, randint

def password_gen():
    pw = [choice(UPPER), choice(LOWER), choice(DIGITS)] + [choice(UPPER+LOWER+DIGITS) for i in range(randint(3, 17))]
    shuffle(pw)
    return "".join(pw)

# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.describe("This is not a real test, just a sample output of your code")

print("Generated password   | Valid?")
print("---------------------|-------")
for _ in range(40):
    pwd = password_gen()
    lower = any(c.islower() for c in pwd)
    upper = any(c.isupper() for c in pwd)
    number = any(c.isdigit() for c in pwd)

    print("%-20s | %s!" %
        ( pwd, ["INVALID", "OK"][ 6 <= len(pwd) <= 20 and lower and upper and number]) )

test.expect(True)