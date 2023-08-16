-- Lists all cities with their state names
SELECT cities.id, cities.name, states.name
  FROM cities
       NATURAL JOIN states
 ORDER BY cities.id;
