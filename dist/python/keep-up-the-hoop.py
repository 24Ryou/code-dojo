# https://www.codewars.com/kata/55cb632c1a5d7b3ad0000145
# --------------------------------- SOLUTION --------------------------------- #
def hoop_count(n):
    if n >= 10 : return 'Great, now move on to tricks' 
    else: return 'Keep at it until you get it' 

def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(hoop_count(3),"Keep at it until you get it" ) 
        test.assert_equals(hoop_count(11),"Great, now move on to tricks" )