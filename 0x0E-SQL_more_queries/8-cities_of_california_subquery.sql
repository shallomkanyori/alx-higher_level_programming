-- Lists all cities of California ordered by cities.id ascending
SELECT id, name
  FROM cities
 WHERE state_id =
       (SELECT id
	  FROM states
	 WHERE name = 'California')
 ORDER BY id;
