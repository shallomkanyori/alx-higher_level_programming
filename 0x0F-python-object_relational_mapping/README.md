## Python - Object-relational mapping

#### Task 0
[0-select_states.py](0-select_states.py) is a script that lists all `states` from a given database (`hbtn_0e_0_usa`).
- Takes 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation performed)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 1
[1-filter_states.py](1-filter_states.py) is a script that lists all `states` with a `name` starting with `N` (upper N) from a database (`hbtn_0e_0_usa`):
- Takes 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation performed)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 2
[2-my_filter_states.py](2-my_filter_states.py) is a script that takes in an argument and displays all values in the `states` table of a given database (`hbtn_0e_0_usa`) where `name` matches the argument.
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation performed)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 3
[3-my_safe_filter_states.py](3-my_safe_filter_states.py) is a script that once again takes in an argument and displays all values in the `states` table of a given database (`hbtn_0e_0_usa`) where `name` matches the argument. But this time, it is safe from MySQL injections.
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 4
[4-cities_by_state.py](4-cities_by_state.py) is a script that lists all `cities` with their `state`'s name from a database (`hbtn_0e_4_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `cities.id`
- Uses `execute()` only once
- Results are displayed one row per line

#### Task 5
[5-filter_cities.py](5-filter_cities.py) is a script that takes in the name of a `state` as an argument and lists all `cities` of that state, using the database (`hbtn_0e_4_usa`)
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (safe from MySQL injection)
- Uses the module `MySQLdb`
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `cities.id`
- Uses `execute()` only once
- Results are displayed separated by a comma and a space
