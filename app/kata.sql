-- https://www.codewars.com/kata/54ff3102c1bad923760001f3
-- -------------------------------- SOLUTION --------------------------------
SELECT str, LENGTH(REGEXP_REPLACE(str, '[^aeiou]', '', 'g')) AS res
FROM getcount