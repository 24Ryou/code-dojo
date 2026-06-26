# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
# --------------------------------- SOLUTION --------------------------------- #
def product_fib(prod):
    a, b = 0, 1
    
    while a * b < prod:
        a, b = b, a + b
    
    return [a, b, a * b == prod]

# ----------------------------------- TEST ----------------------------------- #
print(product_fib(714))
print(product_fib(800))
# import codewars_test as test
