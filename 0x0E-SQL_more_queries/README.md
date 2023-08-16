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

#### Task 8: Cities of California
[8-cities_of_california_subquery.sql](8-cities_of_california_subquery.sql) lists all cities of California ordered by `cities.id` (ascending).

#### Task 9: Cities by States
[9-cities_by_state_join.sql](9-cities_by_state_join.sql) lists all cities in the database `hbtn_0d_usa`.
- Each record displays: `cities.id` - `cities.name` - `states.name`
- Results are sorted in ascending order by `cities.id`
- Uses only one SELECT statement

#### Task 10: Genre ID by show
[10-genre_id_by_show.sql](10-genre_id_by_show.sql) lists all shows in `hbtn_0d_tvshows` that have at least one genre linked.
- Each record displays: `tv_shows.title` - `tv_show_genres.genre_id`
- Results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- Uses only one SELECT statement

#### Genre ID for all shows
[11-genre_id_all_shows.sql](11-genre_id_all_shows.sql) lists all shows contained in the database `hbtn_0d_tvshows`.
- Each record displays: `tv_shows.title` - `tv_show_genres.genre_id`
- Results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- If a show doesn’t have a genre, displays NULL
- Uses only one SELECT statement

#### Task 12. No genre
[12-no_genre.sql](12-no_genre.sql) lists all shows contained in the database `hbtn_0d_tvshows` without a genre linked.
- Each record displays: `tv_shows.title` - `tv_show_genres.genre_id`
- Results are sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- If a show doesn’t have a genre, displays NULL
- Uses only one SELECT statement

#### Task 13: Number of shows by genre
[13-count_shows_by_genre.sql](13-count_shows_by_genre.sql) lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
- Each record displays: `<TV Show genre>` - `<Number of shows linked to this genre>`
- First column is called `genre`
- Second column is called `number_of_shows`
- Doesn’t display a genre that doesn’t have any shows linked
- Results are sorted in descending order by the number of shows linked

#### Task 14: My genres
[14-my_genres.sql](14-my_genres.sql) lists all genres of the show `Dexter` by name from the `hbtn_0d_tvshows`.
- Each record displays: `tv_genres.name`
- Results are sorted in ascending order by the genre name
- Uses only one `SELECT` statement

#### Task 15: Only Comedy
[15-comedy_only.sql](15-comedy_only.sql) lists all Comedy shows in the database `hbtn_0d_tvshows`.
- Each record displays: `tv_shows.title`
- Results area sorted in ascending order by the show title
- Uses only one `SELECT` statement

#### Task 16: Lists shows and genres
[16-shows_by_genre.sql](16-shows_by_genre.sql)  lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
- If a show doesn’t have a genre, displays `NULL` in the genre column
- Each record displays: `tv_shows.title` - `tv_genres.name`
- Results are sorted in ascending order by the show title and genre name
- Uses only one `SELECT` statement


#### Task 17: Not my genre
[100-not_my_genres.sql](100-not_my_genres.sql) list all genres not linked to the show `Dexter` from the `hbtn_0d_tvshows` database.
- Each record displays: `tv_genres.name`
- Results are sorted in ascending order by the genre name
- Uses a maximum of two `SELECT` statement
