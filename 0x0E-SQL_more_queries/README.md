## SQL - More queries

#### Task 0: My privileges!
[0-privileges.sql](0-privileges.sql) lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` (in `localhost`)

#### Task 1: Root user
[1-create_user.sql](1-create_user.sql) creates the MySQL server user `user_0d_1` if this user doesn't already exist.
- `user_0d_1` has all privileges on the server
- `user_0d_1` password is set to `user_0d_1_pwd`

#### Task 2: Read user
[2-create_read_user.sql](2-create_read_user.sql) creates the database `hbtn_0d_2` and the user `user_0d_2` if they don't already exist.
- `user_0d_2` has only the SELECT privilege in the database `hbtn_0d_2`
- The `user_0d_2` password is set to `user_0d_2_pwd`

#### Task 3: Always a name
[3-force_name.sql](3-force_name.sql) creates the table `force_name` in the current database if it doesn't already exist.
- `force_name` description
	- `id` INT
	- `name` VARCHAR(256) can't be null

#### Task 4: ID can't be null
[4-never_empty.sql](4-never_empty.sql) creates the table `id_not_null` in the current database if it doesn't already exist.
- `id_not_null` description
	- `id` INT with the default value `1`
	- `name` VARCHAR(256)

#### Task 5: Unique ID
[5-unique_id.sql](5-unique_id.sql) creates the table `unique_id` in the current database if it doesn't already exist.
- `unique_id` description
	- `id` INT with the default value `1` and must be unique
	- `name` VARCHAR(256)

#### Task 6: States table
[6-states.sql](6-states.sql) creates the database `hbtn_0d_usa` and the table `hbtn_0d_usa.states` if they don't already exist.
- `states` description
	- `id` INT unique, auto generated, can't be null and is a primary key
	- `name` VARCHAR(256) can't be null

#### Task Cities table
[7-cities.sql](7-cities.sql) creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d-usa`) if they don't already exist.
- `cities` description
	- `id` INT unique, auto generated, can't be null and is a primary key
	- `state_id` INT, can't be null and must be a `FOREIGN KEY` that references `id` of the `states` table
	- `name` VARCHAR(256) can't be null
