# https://www.codewars.com/kata/555eded1ad94b00403000071
# --------------------------------- SOLUTION --------------------------------- #
def series_sum(n):
    base_div = 1
    total_sum = 0
    for i in range(n):
        total_sum += 1/(base_div) 
        base_div += 3
    return "{:.2f}".format(total_sum)

# 2nd way
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
test.assert_equals(series_sum(1), "1.00")
test.assert_equals(series_sum(2), "1.25")
test.assert_equals(series_sum(3), "1.39")