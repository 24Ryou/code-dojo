-- https://www.codewars.com/kata/591127cbe8b9fb05bd00004b
-- -------------------------------- SOLUTION --------------------------------
select name, author, copies_sold
from books
order by copies_sold desc
limit 5;