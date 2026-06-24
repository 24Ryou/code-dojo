# https://www.codewars.com/kata/5503013e34137eeeaa001648
# --------------------------------- SOLUTION --------------------------------- #
def diamond(n):
    # 1. Handle invalid cases
    if n < 1 or n % 2 == 0:
        return None
    
    m = n // 2
    res = ""
    
    # 2. Build the string
    for i in range(n):
        # The number of spaces is the distance from the middle row
        spaces = abs(m - i)
        
        # The number of stars decreases as we move away from the middle
        stars = n - (2 * spaces)
        
        res += (' ' * spaces) + ('*' * stars) + '\n'
        
    return res


print(diamond(5))
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
