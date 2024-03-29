## SQL - Introduction

#### Task 0: List databases
[0-list_databases.sql](0-list_databases.sql) is a script that lists all databases of the MySQL server.

#### Task 1: Create a database
[1-create_database_if_missing.sql](1-create_database_if_missing.sql) creates the database `hbtn_0c_0` if it does not already exist.

#### Task 2: Delete a database
[2-remove_database.sql](2-remove_database.sql) deletes the database `hbtn_0c_0` if it exists.

#### Task 3: List tables
[3-list_tables.sql](3-list_tables.sql) lists all the tables of the current database.

###Task 4: First table
[4-first_table.sql](4-first_table.sql) creates a table called `first_table` in the current database if it doesn't already exist.
- `first_table` description:
	- `id` INT
	- `name` VARCHAR(256)

#### Task5 5: Full description
[5-full_table.sql](5-full_table.sql) prints the full description of the table `first_table` from the current database (assumed to be `hbtn_0c_0`).
- Does not use the `DESCRIBE` or `EXPLAIN` statements.

#### Task 6: List all in table
[6-list_values.sql](6-list_values.sql) lists all rows of the table `first_table` from the current database (assumed to be `hbtn_0c_0`).

#### Task 7: First add
[7-insert_value.sql](7-insert_value.sql) inserts a new row in the table `first_table` (database `hbtn_0c_0`).
- New row:
	- `id` = `89`
	- `name` = `Best School`

#### Task 8: Count 89
[8-count_89.sql](8-count_89.sql) displays the number of records with `id = 89` in the table `first_table` (database `hbtn_0c_0`).

#### Task 9: Full creation
[9-full_creation.sql](9-full_creation.sql) creates a table `second_table` in the current database (`hbtn_0c_0`) if it doesn't exist and adds 4 records.
- `second_table` description
	- `id` INt
	- `name` VARCHAR(256)
	- `score` INT
- Creates these records:
	- `id` = 1, `name` = "John", `score` = 10
	- `id` = 2, `name` = "Alex", `score` = 3
	- `id` = 3, `name` = "Bob", `score` = 14
	- `id` = 4, `name` = "George", `score` = 8

#### Task 10: List by best
[10-top_score.sql](10-top_score.sql)  lists all records of the table `second_table` (database `hbtn_0c_0`)
- Displays both the score and the name (in this order)
- Records are ordered by score (top first)

#### Task 11: Select the best
[11-best_score.sql](11-best_score.sql) lists all records with a `score >= 10` in the table `second_table` (database `hbtn_0c_0`).
- Displays both the score and the name (in this order)
- Records are ordered by the score (top first)

#### Task 12: Cheating is bad
[12-no_cheating.sql](12-no_cheating.sql) updates the score of Bob to `10` in the table `second_table`.

#### Task 13: Score too low
[13-change_class.sql](13-change_class.sql) removes all records with a `score <= 5` in the table `second_table` (database `hbtn_0c_0`).

#### Task 14: Average
[14-average.sql](14-average.sql) computes the score average of all records in the table `second_table` (database `hbtn_0c_0`).
- The result column name is `average`.

#### Task 15: Number by score
[15-groups.sql](15-groups.sql) lists the number of records with the same score in the table `second_table` (database `hbtn_0c_0`).
- The result displays:
	- the `score`
	- the number of records for this `score` with the label `number`
- The list is sorted by the number of records (descending)

#### Task 16: Say my name
[16-no_link.sql](16-no_link.sql) lists all records of the table `second_table` (database `hbtn_0c_0`).
- Doesn't list rows without a `name` value
- Displays the score and the name (in this order)
- Records are listed by descending score

#### Task 17: Go to UTF8
[100-move_to_utf8.sql](100-move_to_utf8.sql) converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`).
Converts all of the following to `UTF8`:
- Database `hbtn_0c_0`
- Table `first_table`
- Field `name` in `first_table`

#### Task 18: Temperatures #0
Import the `temperatures` table into `hbtn_0c_0` database.

[101-avg_temperatures.sql](101-avg_temperatures.sql) displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

#### Task 19: Temperatures #1
[102-top_city.sql](102-top_city.sql) displays the top 3 of cities temperature during July and August ordered by temperature (descending).

#### Task 20: Temperatures #2
[103-max_state.sql](103-max_state.sql) displays the max temperature of each state ordered by state name.
