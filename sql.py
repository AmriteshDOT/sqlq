# Order of execution->
= FROM - JOIN - WHERE - GROUP BY - Aggregations(maths sum(),avg(),etc inside buckets) - HAVING - SELECT - DISTINCT(internal step) - ORDER BY - LIMIT
= THINK columns as vectors
= SELECT makes the "virtual table" on the fly & never changes your actual database structure
= SELECT *,something as som => all table and also a 'som' column appended at the last
= SELECT *, DISTINCT(something) as som : error (contradicting : as * means show me all , DISTINCT means collapse duplicate rows also )
= DISTINCT : filter DISTINCT just to get final unique results and not the other infos right : DISTINCT is lossy. By choosing to use it, you are telling SQL, "I don't care about the specific details of the rows I'm throwing away; I only care about the unique values that remain." say we have 4 columns and we do distinct on column2 , then only distinct values of column2 remain in a single column and rest data like col1,3,4 is just lost now 
= GROUP BY : is like a bucket where we may perform different operations
#==============
1. {int} , {enum}(yes/no) : { WHERE } row filter
2. referee_id!=2 or referee_id IS NULL (like x==5 or x==6 , not like x==5 or 6) : WHEN WE FILTER (NULL ones are gone , so we needa save them)
    varchar = takes size of entered string although assigned maxLength
3.{ bigInt } is like long long
4.{ date } 
5.Scalar functions(row wise) : LENGTH(content), UPPER(), ROUND(), ABS()  : Aggregation functions(bucket) : SUM(), COUNT(), AVG(), MAX() | LENGTH() used here