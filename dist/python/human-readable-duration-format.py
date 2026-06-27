# https://www.codewars.com/kata/52742f58faf5485cae000b9a
# --------------------------------- SOLUTION --------------------------------- #
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
YEAR = 365 * DAY


def format_duration(seconds):
    yrs = seconds // YEAR
    dys = (seconds % YEAR) // DAY
    hrs = (seconds % DAY) // HOUR
    mins = (seconds % HOUR) // MINUTE
    secs = (seconds % MINUTE)
    res = []
    if seconds == 0:
        res.append('now')
    if yrs > 0:
        res.append(f"{yrs} {'year'if yrs == 1 else 'years'}")
    if dys > 0:
        res.append(f"{dys} {'day'if dys == 1 else 'days'}")
    if hrs > 0:
        res.append(f"{hrs} {'hour'if hrs == 1 else 'hours'}")
    if mins > 0:
        res.append(f"{mins} {'minute'if mins == 1 else 'minutes'}")
    if secs > 0:
        res.append(f"{secs} {'second'if secs == 1 else 'seconds'}")

    if len(res) > 1:
        return ', '.join(res[:-1]) + ' and ' + res[-1]
    else:
        return res[0]

# 2nd way - optimize + correctness
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR
YEAR = 365 * DAY


def format_duration(seconds):
    if seconds == 0:
        return "now"

    yrs = seconds // YEAR
    seconds %= YEAR

    dys = seconds // DAY
    seconds %= DAY

    hrs = seconds // HOUR
    seconds %= HOUR

    mins = seconds // MINUTE
    secs = seconds % MINUTE

    res = []

    if yrs > 0:
        res.append(f"{yrs} {'year' if yrs == 1 else 'years'}")
    if dys > 0:
        res.append(f"{dys} {'day' if dys == 1 else 'days'}")
    if hrs > 0:
        res.append(f"{hrs} {'hour' if hrs == 1 else 'hours'}")
    if mins > 0:
        res.append(f"{mins} {'minute' if mins == 1 else 'minutes'}")
    if secs > 0:
        res.append(f"{secs} {'second' if secs == 1 else 'seconds'}")

    if len(res) == 1:
        return res[0]

    return ', '.join(res[:-1]) + ' and ' + res[-1]

# ----------------------------------- TEST ----------------------------------- #
# import codewars_test as test
tests = [
    (0, "now"),
    (1, "1 second"),
    (2, "2 seconds"),
    (60, "1 minute"),
    (62, "1 minute and 2 seconds"),
    (120, "2 minutes"),
    (3600, "1 hour"),
    (3662, "1 hour, 1 minute and 2 seconds"),
    (86400, "1 day"),
    (31536000, "1 year"),
    (31536000 + 86400 + 3600 + 60 + 1,
     "1 year, 1 day, 1 hour, 1 minute and 1 second"),
]

for (x, res) in tests:
    print(res, format_duration(x), format_duration(x) == res)
# print(tests[7][1], f'\nout : {format_duration(tests[7][0])}', f'\n{format_duration(tests[7][0]) == tests[7][1]}')
