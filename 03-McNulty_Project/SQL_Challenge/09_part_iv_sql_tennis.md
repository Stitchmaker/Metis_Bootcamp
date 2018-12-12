# Challenge Set 9
## Part IV: Tennis Data

### 1. Using the same tennis data, find the number of matches played by each player in each tournament. (Remember that a player can be present as both player1 or player2).
```sql
SELECT new_table.player, COUNT(new_table.player) as matches
FROM
(
      SELECT player1 AS player
      FROM us_men_2013
      UNION ALL
      SELECT player2 AS player
      FROM us_men_2013
) new_table
GROUP BY new_table.player;

```

### 2. Who has played the most matches total in all of US Open, AUST Open, French Open? Answer this both for men and women.
```sql
SELECT new_table.player, COUNT(new_table.player) as matches
FROM
(
      SELECT player1 AS player
      FROM us_men_2013
      UNION ALL
      SELECT player2 AS player
      FROM us_men_2013
      UNION ALL
      SELECT player1 AS player
      FROM aus_men_2013
      UNION ALL
      SELECT player2 AS player
      FROM aus_men_2013
      UNION ALL
      SELECT player1 AS player
      FROM french_men_2013
      UNION ALL
      SELECT player2 AS player
      FROM french_men_2013
) new_table
GROUP BY new_table.player
ORDER BY matches DESC
LIMIT 1;
```
For the men, Rafael Nadal played the most matches at 21

```sql
SELECT new_table.player, COUNT(new_table.player) as matches
FROM
(
      SELECT player1 AS player
      FROM us_ladies_2013
      UNION ALL
      SELECT player2 AS player
      FROM us_ladies_2013
      UNION ALL
      SELECT player1 AS player
      FROM aus_ladies_2013
      UNION ALL
      SELECT player2 AS player
      FROM aus_ladies_2013
      UNION ALL
      SELECT player1 AS player
      FROM french_ladies_2013
      UNION ALL
      SELECT player2 AS player
      FROM french_ladies_2013
) new_table
GROUP BY new_table.player
ORDER BY matches DESC
LIMIT 1;
```
For the ladies, Agnieszka Radwanska played the most matches at 17

### 3. Who has the highest first serve percentage? (Just the maximum value in a single match.)
```sql
SELECT new_table.player, MAX(new_table.fsp) as first_serve_per
FROM
(
      SELECT player1 AS player, fsp_1 AS fsp
      FROM us_ladies_2013
      UNION ALL
      SELECT player2 AS player, fsp_2 AS fsp
      FROM us_ladies_2013
      UNION ALL
      SELECT player1 AS player, fsp_1 AS fsp
      FROM aus_ladies_2013
      UNION ALL
      SELECT player2 AS player, fsp_2 AS fsp
      FROM aus_ladies_2013
      UNION ALL
      SELECT player1 AS player, fsp_1 AS fsp
      FROM french_ladies_2013
      UNION ALL
      SELECT player2 AS player, fsp_2 AS fsp
      FROM french_ladies_2013
) new_table
GROUP BY new_table.player
ORDER BY first_serve_per DESC
LIMIT 1;
```
For the women, S Errani has the highest first serve percentage at 93%.   

```sql
SELECT new_table.player, MAX(new_table.fsp) as first_serve_per
FROM
(
      SELECT player1 AS player, fsp_1 AS fsp
      FROM us_men_2013
      UNION ALL
      SELECT player2 AS player, fsp_2 AS fsp
      FROM us_men_2013
      UNION ALL
      SELECT player1 AS player, fsp_1 AS fsp
      FROM aus_men_2013
      UNION ALL
      SELECT player2 AS player, fsp_2 AS fsp
      FROM aus_men_2013
      UNION ALL
      SELECT player1 AS player, fsp_1 AS fsp
      FROM french_men_2013
      UNION ALL
      SELECT player2 AS player, fsp_2 AS fsp
      FROM french_men_2013
) new_table
GROUP BY new_table.player
ORDER BY first_serve_per DESC
LIMIT 1;
```
For the women, Carlos Berlocq has the highest first serve percentage at 84%

### 4. What are the unforced error percentages of the top three players with the most wins? (Unforced error percentage is % of points lost due to unforced errors. In a match, you have fields for number of points won by each player, and number of unforced errors for each field.)

*Hint:* `SUM(double_faults)` sums the contents of an entire column. For each row, to add the field values from two columns, the syntax `SELECT name, double_faults + unforced_errors` can be used.

```sql
SELECT new_table.player, COUNT(new_table.player) as matches, uep
FROM
(
      SELECT player1 AS player, ufe_1/fnl2 AS uep
      FROM us_men_2013
      WHERE result = 0
      UNION ALL
      SELECT player2 AS player, ufe_2/fnl1 AS uep
      FROM us_men_2013
      WHERE result = 1
      UNION ALL
      SELECT player1 AS player, ufe_1/fnl2 AS uep
      FROM aus_men_2013
      WHERE result = 0
      UNION ALL
      SELECT player2 AS player, ufe_2/fnl1 AS uep
      FROM aus_men_2013
      WHERE result = 1
      UNION ALL
      SELECT player1 AS player, ufe_1/fnl2 AS uep
      FROM french_men_2013
      WHERE result = 0
      UNION ALL
      SELECT player2 AS player, ufe_2/fnl1 AS uep
      FROM french_men_2013
      WHERE result = 1
) new_table
GROUP BY new_table.player, uep
ORDER BY matches DESC
LIMIT 3;
```
For the men, Edouard Roger-Vasselin with 11.3%, Richard Gasquet with 11.3% and Tommy Haas with 0%.

```sql
SELECT new_table.player, COUNT(new_table.player) as matches, uep
FROM
(
      SELECT player1 AS player, ufe_1/fnl2 AS uep
      FROM us_ladies_2013
      WHERE result = 0
      UNION ALL
      SELECT player2 AS player, ufe_2/fnl1 AS uep
      FROM us_ladies_2013
      WHERE result = 1
      UNION ALL
      SELECT player1 AS player, ufe_1/fnl2 AS uep
      FROM aus_ladies_2013
      WHERE result = 0
      UNION ALL
      SELECT player2 AS player, ufe_2/fnl1 AS uep
      FROM aus_ladies_2013
      WHERE result = 1
      UNION ALL
      SELECT player1 AS player, ufe_1/fnl2 AS uep
      FROM french_ladies_2013
      WHERE result = 0
      UNION ALL
      SELECT player2 AS player, ufe_2/fnl1 AS uep
      FROM french_ladies_2013
      WHERE result = 1
) new_table
GROUP BY new_table.player, uep
ORDER BY matches DESC
LIMIT 3;
```
For the women, Svetlana Kuznetsova with 12%, Lucie Safarova with 21.5% and Monica Niculescu with 17%.

*Special bonus hint:* To be careful about handling possible ties, consider using [rank functions](http://www.sql-tutorial.ru/en/book_rank_dense_rank_functions.html).
