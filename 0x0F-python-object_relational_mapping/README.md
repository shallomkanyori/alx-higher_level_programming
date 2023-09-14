## Python - Object-relational mapping

#### Task 0
[0-select_states.py](0-select_states.py) is a script that lists all `states` from a given database.
- Takes 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation performed)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 1
[1-filter_states.py](1-filter_states.py) is a script that lists all `states` with a `name` starting with `N` (upper N) from a database:
- Takes 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation performed)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 2
[2-my_filter_states.py](2-my_filter_states.py) is a script that takes in an argument and displays all values in the `states` table of a given database where `name` matches the argument.
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation performed)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 3
[3-my_safe_filter_states.py](3-my_safe_filter_states.py) is a script that once again takes in an argument and displays all values in the `states` table of a given database where `name` matches the argument. But this time, it is safe from MySQL injections.
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

