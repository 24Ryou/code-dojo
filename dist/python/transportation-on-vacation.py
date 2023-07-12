# https://www.codewars.com/kata/568d0dd208ee69389d000016
# --------------------------------- SOLUTION --------------------------------- #
def rental_car_cost(d):
    # 40 every day
    # for 7 days or more -50 off for 3 days or more -20 off
    return d * 40 - (50 if d >= 7 else 20 if d >= 3 else 0)
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
@test.it('Basic Test Cases')
def basic_test_cases():
    test.assert_equals(rental_car_cost(1),40)
    test.assert_equals(rental_car_cost(4),140)
    test.assert_equals(rental_car_cost(7),230)
    test.assert_equals(rental_car_cost(8),270)
