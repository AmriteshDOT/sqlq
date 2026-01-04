# Order of execution->
= FROM(table alias born AS) - JOIN - WHERE - GROUP BY - Aggregations(maths sum(),avg(),etc inside buckets) - HAVING - SELECT(column aliases born AS) - DISTINCT(internal step) - ORDER BY - LIMIT
= THINK columns as vectors
= SELECT makes the "virtual table" on the fly & never changes your actual database structure
= SELECT *,something as som => all table and also a 'som' column appended at the last
= SELECT *, DISTINCT(something) as som : error (contradicting : as * means show me all , DISTINCT means collapse duplicate rows also )
= DISTINCT : filter DISTINCT just to get final unique results and not the other infos right : DISTINCT is lossy. By choosing to use it, you are telling SQL, "I don't care about the specific details of the rows I'm throwing away; I only care about the unique values that remain." say we have 4 columns and we do distinct on column2 , then only distinct values of column2 remain in a single column and rest data like col1,3,4 is just lost now 
= GROUP BY : is like a bucket where we may perform different operations
= COUNT(*) counts every row , COUNT(phoneNumber) this ignores the NULL.
= 'date' specific fucntions : DATEDIFF(end,start) returns 'DAYS' values.
= if many different join conditions , connect them with 'and'   (WHERE , ON , HAVING) "Both Condition A and Condition B must be met."
= GROUP BY and ORDER BY when done using different columns those are separated using ',' (GROUP BY , ORDER BY , SELECT). "Do this for Column A, then Column B, then Column C."
= Use CTEs : with tmp as ()
= when we join and 2 tables have same column name then after join if we write that column name thats in both tables , it throws an error (COLUMN AMBIGUITY) : so always use aliases in those scenarios
= when we GROUPBY (NULL hve its own bucket). COUNT(*) counts NULL values , In JOIN (Standard): NULL does not match NULL, so the data usually disappears at this step.(but its always better and cleaner to remove NULL initially as those arent the answers anyways.)
=(CASE WHEN ..) make another column : named (CASE WHEN ...) unless its aliased , as we can do things on it .
= !=(not equals) (id%2 means odd)
=between in DATE(data type) gives inclusive dates
= CASE WHEN used when decisions based on data(if-else) , but COALESCE used when we need to fill NULLs. Its like pandas.fillna()
= so 1 row * 1 column is scalar, 1 column is List, and rows*column is table (scalar:used as filter or simple math helper, list:used form IN,ANY,ALL , table is like table thats it.)[1X1 is a scalar , NX1 is a list , NXM is a table.]
#==============
1. {int} , {enum}(yes/no) : { WHERE } row filter
2. referee_id!=2 or referee_id IS NULL (like x==5 or x==6 , not like x==5 or 6) : WHEN WE FILTER (NULL ones are gone , so we needa save them)
    varchar = takes size of entered string although assigned maxLength
3.{ bigInt } is like long long
4.{ date } 
5.Scalar functions(row wise) : LENGTH(content), UPPER(), ROUND(), ABS()  : Aggregation functions(bucket) : SUM(), COUNT(), AVG(), MAX() | LENGTH() used here
#JOINS
6.i think of left join as a) inner join first , then b) add missing left rows with null of right table .(LEFT JOIN always have >= rows in left table) [[ LEFT JOIN - ON ]]
7.-
8.SELECT is the place that know what needs to be served , (maths , aggregates , DISTINCT , newColumns : are born there) [[ SQL knows the order ]]  ::: COUNT(*) is a common way , instead of anyParticular column we use *.
9.ON DATEDIFF(w2.recordDate , w1.recordDate)=1 (join using 'date' specific fucntions : DATEDIFF(end,start))
10.JOINS : if many different join conditions , connect them with 'and'
11.
12.CROSS JOIN for all combinations (aXb) learn joins . COUNT such that NULL of a column is 0 . DO count(column) instead of COUNT(*)
13.groupBY (managerID): NULL is also grouped also counted by COUNT(*). but its always better and cleaner to remove NULL initially as those arent the answers anyways.
14.JOIN + CASE WHEN
#Aggregates
15.odd and !=boring
16.between in DATE(data type) gives inclusive dates + coalesce to fillna , CASE WHEN used for if-else not efficient for the NULL fills
17.
18. 1X1 is a scalar , NX1 is a list , NXM is a table.