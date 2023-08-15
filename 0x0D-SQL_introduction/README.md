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
