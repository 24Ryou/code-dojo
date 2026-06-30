# https://www.codewars.com/kata/514a024011ea4fb54200004b
# --------------------------------- SOLUTION --------------------------------- #
import re
# Explanation:
# (?:https?://)?   -> Optional protocol (http or https)
# (?:www\.)?       -> Optional "www."
# ([a-zA-Z0-9.-]+) -> Capture group for the domain name
def domain_name(url):
    match = re.search(r"(?:https?://)?(?:www\.)?([a-zA-Z0-9-]+)\.", url)

    if match:
        return match.group(1)
    
# 2nd way
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

# 3rd way
def domain_name(url):
    url = url.split("//")[-1]
    url = url.replace("www.", "")
    return url.split(".")[0]
# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
print(domain_name('http://www.codewars.com/kata/'))
print(domain_name('https://hyphen-site.org'))
print(domain_name('http://google.co.jp'))
print(domain_name('cnn.org'))