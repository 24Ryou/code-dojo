# https://www.codewars.com/kata/57b06f90e298a7b53d000a86
# --------------------------------- SOLUTION --------------------------------- #
def queue_time(customers, n):
    tills = [0] * n

    for customer in customers:
        i = tills.index(min(tills))
        tills[i] += customer

    return max(tills)

# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test


@test.describe("The Supermarket Queue")
def the_supermarket_queue():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
        test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
        test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
        test.assert_equals(queue_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")
        test.assert_equals(queue_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")
        test.assert_equals(queue_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")
    
# add your own test cases here