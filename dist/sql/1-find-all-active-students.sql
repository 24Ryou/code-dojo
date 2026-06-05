-- https://www.codewars.com/kata/5809b9ef88b750ab180001ec
-- -------------------------------- SOLUTION --------------------------------
select
    s.id,
    s.firstname,
    s.lastname,
    s.isactive
from
    students s
where
    s.isactive = TRUE
order by
    s.id