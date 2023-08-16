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
