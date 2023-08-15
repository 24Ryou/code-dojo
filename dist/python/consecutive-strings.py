# https://www.codewars.com/kata/56a5d994ac971f1ac500003e
# --------------------------------- SOLUTION --------------------------------- #
def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""
    else:
        arr = ["".join(strarr[i:i + k]) for i in range(len(strarr) - k + 1)]
        ans = arr[0]
        for word in arr:
            if len(word) > len(ans):
                ans = word
        return ans
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test

test.assert_equals(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
test.assert_equals(
    longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1),
    "oocccffuucccjjjkkkjyyyeehh")
test.assert_equals(longest_consec([], 3), "")
test.assert_equals(
    longest_consec(["itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2),
    "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
test.assert_equals(longest_consec(["wlwsasphmxx", "owiaxujylentrklctozmymu", "wpgozvxxiu"], 2),
                   "wlwsasphmxxowiaxujylentrklctozmymu")
test.assert_equals(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
test.assert_equals(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
test.assert_equals(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
test.assert_equals(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
