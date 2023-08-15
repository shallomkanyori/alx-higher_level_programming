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
