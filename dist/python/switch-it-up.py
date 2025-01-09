# https://www.codewars.com/kata/5808dcb8f0ed42ae34000031
# --------------------------------- SOLUTION --------------------------------- #
def switch_it_up(number):
    d = {0 : 'Zero',
         1 : 'One',
         2 : 'Two',
         3 : 'Three',
         4 : 'Four',
         5 : 'Five',
         6 : 'Six',
         7 : 'Seven',
         8 : 'Eight',
         9 : 'Nine'}

    return d.get(number)

def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(switch_it_up(0), "Zero")
        test.assert_equals(switch_it_up(9), "Nine")