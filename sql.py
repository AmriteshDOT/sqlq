# Order of execution->
= FROM(table alias born AS) - JOIN - WHERE - GROUP BY - Aggregations(maths distinct(hereAlso),sum(),avg(),etc inside buckets) - HAVING - SELECT(column aliases born AS) - DISTINCT(internal step) - ORDER BY - LIMIT
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
= DATE_FROMPART(date,'year'/'month'/'day') to extract parts of date (M=monthName , m=monthNumber); basically (DATE_FORMAT) acts like a fstring in python but instead of {} we use %
= minimum of each group = GROUPBY then MIN(column) , date also
= datediff between 0 and 29 (means 0,1,2..29) means last 30 days considered if we do (between 0 and 30) its 31 days.(OR datediff>=0 and datediff<30).
= Aggregates Rule:The "Total Table" Mode (No GROUP BY):If the table has data:we get 1 row(answer).table is EMPTY: You still get 1 row.NULL (for SUM, MAX, AVG) or 0 (for COUNT).
 In (GROUP BY):if the table is EMPTY: There are no groups. If there are no groups, there are no rows. Result: You get 0 rows (an empty result set).
 Stacking (UNION ALL/UNION):unionall quicker(no duplicate checks) [3 rules: Same Number of Columns,compatible data types, order of columns must match] : Make NULL to match
=so means there are 2 distincts , a) groupBY bucket maths distinct b) Select maths distinct 
=(CASE WHEN (x+y>z AND y+z>x AND x+z>y) THEN 'Yes' ELSE 'No' END) as triangle [sinple maths here]
=to make all the rows a constant use , <constant> as row . (constants can be a) number b)string c)date )
=we use ORDERBY in window functions : so to make the rank/total running.(running Rank/Total = window function usage)
=with table (c1,c2) as (VALUES ROW(r11,r12),ROW(r21,r22),row(r31,r32)).*
=.comparison with NULL is UNKNOWN ,WHERE clause only keeps TRUE ,UNKNOWN !=TRUE so those are filtered out. WHERE manager_id is NOT NULL AND manager_id not in (SELECT employee_id FROM Employees) , manager_id is NOT NULL is this redundant
=subquery of size can be used somewhere (SELECT count(*) FORM table) as a number logic.
=WHERE DATE_FORMAT(created_at,'%Y-%m')='2020-02' && WHERE created_at>='2020-02-01' AND created_at <'2020-03-01' (date_format is slower)
= sum(sm) OVER (ORDER BY visited_on ROWS between 6 preceding AND current row ) , DATE_ADD((SELECT min(visited_on) FROM runsm),INTERVAL 6 DAY) : to get date ahead of some day DATE_ADD(opp is DATE_SUB) : as inclusive kinda
= DENSE RANK() (PARTITION BY - ORDER BY)
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
19.basic maths (inside GROUP bucket)
20.DATE_FORMAT , this is fstring with {} as %
21.CTE:minDate for each , JOIN (id+firstDate)
22.CTE:minDate for each , JOIN (id+datefiff=1)
#Sort+group
23.
24.datediff between 0 and 29 (means 0,1,2..29) means last 30 days considered if we do (between 0 and 30) its 31 days.(OR datediff>=0 and datediff<30)
25.min(date) and join(id+mindate)
26.groupby class having count(*)>=5
27.
28.= Aggregates Rule:The "Total Table" Mode (No GROUP BY):If the table has data:we get 1 row(answer).table is EMPTY: You still get 1 row.NULL (for SUM, MAX, AVG) or 0 (for COUNT).
 In (GROUP BY):if the table is EMPTY: There are no groups. If there are no groups, there are no rows. Result: You get 0 rows (an empty result set).
 Stacking (UNION ALL/UNION):unionall quicker(no duplicate checks) [3 rules: Same Number of Columns,compatible data types, order of columns must match] : Make NULL to match
29.so means there are 2 distincts , a) groupBY bucket maths distinct b) Select maths distinct [here we have used bucket distinct]
#advanced SELECT and JOINS
30.basics
31.did using UNIONALL ; one table for single, another with primary='Y' : Then union all
32.SELECT x,y,z,(CASE WHEN (x+y>z AND y+z>x AND x+z>y) THEN 'Yes' ELSE 'No' END) as triangle FROM Triangle
33.3 joins
34.2 phases CTE (before and after) then JOIN. (10 as price : constant used to fill all rows as 10)
35.window function (sum() over (order rank)) : Order = running rank&total36
36.selfmade CTE : with table (c1,c2) as (VALUES ROW(r11,r12),ROW(r21,r22),row(r31,r32)).
#subqueries
37.comparison with NULL is UNKNOWN ,WHERE clause only keeps TRUE ,UNKNOWN !=TRUE so those are filtered out. WHERE manager_id is NOT NULL AND manager_id not in (SELECT employee_id FROM Employees) , manager_id is NOT NULL is this redundant
38.we have to care for table size (subquery of size.)
39.WHERE DATE_FORMAT(created_at,'%Y-%m')='2020-02' && WHERE created_at>='2020-02-01' AND created_at <'2020-03-01' (date_format is slower)
40.= sum(sm) OVER (ORDER BY visited_on ROWS between 6 preceding AND current row ) , DATE_ADD((SELECT min(visited_on) FROM runsm),INTERVAL 6 DAY) : to get date ahead of some day DATE_ADD
41.unionALL is the new best friend and LIMIT 1
42.CTE game (2 CTE + implementations)
43.dense RANK() OVER (PARTITION BY ORDER BY)