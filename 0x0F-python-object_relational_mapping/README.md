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

#### Task 6
[model_state.py](model_state.py) contains the class definition of a `State` and an instance `Base = declarative_base()`:
- `State` class:
	- inherits from `Base`
	- links to the MySQL table `states`
	- class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	- class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
- Uses the module `SQLAlchemy`
- Scripts should connect to a MySQL server running on `localhost` at port `3306`

#### Task 7
[7-model_state_fetch_all.py](7-model_state_fetch_all.py) is a script that lists all `State` objects from a database (`hbtn_0e_6_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 8
[8-model_state_fetch_first.py](8-model_state_fetch_first.py) is a script that prints the first `State` object from a database (`hbtn_0e_6_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
- Result is displayed as `<state.id>: <state.name>`
- If the table `states` is empty, prints `Nothing` followed by a new line

#### Task 9
[9-model_state_filter_a.py](9-model_state_filter_a.py) is script that lists all `State` objects that contain the letter `a` from a database (`hbtn_0e_6_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
- Results are sorted in ascending order by `states.id`
- Results are displayed one row per line

#### Task 10
[10-model_state_my_get.py](10-model_state_my_get.py) is a script that prints the `State` object with the `name` passed as argument from a database (`hbtn_0e_6_usa`)
- Takes 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (MySQL injection free)
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
- Assumes there is only one record with the state name to search
- Result displays the `states.id`
- If no state has the name that was searched for, displays `Not found`

#### Task 11
[11-model_state_insert.py](11-model_state_insert.py) is a script that adds the `State` object “Louisiana” to a database (`hbtn_0e_6_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
- Prints the new `states.id` after creation

#### Task 12
[12-model_state_update_id_2.py](12-model_state_update_id_2.py) is a script that changes the name of a `State` object from a database (`hbtn_0e_6_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
- Changes the name of the `State` where `id = 2` to `New Mexico`

#### Task 13
[13-model_state_delete_a.py](13-model_state_delete_a.py) is a script that deletes all `State` objects with a name containing the letter `a` from a database (`hbtn_0e_6_usa`)
- Takes 3 arguments: `mysql username`, `mysql password` and `database name`
- Uses the module `SQLAlchemy`
- Imports `State` and `Base` from [model_state.py](model_state.py)
- Connects to a MySQL server running on `localhost` at port `3306`
