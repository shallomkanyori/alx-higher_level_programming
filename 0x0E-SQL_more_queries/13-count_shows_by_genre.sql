-- Lists all genres and the number of shows linked to each
SELECT tg.name AS genre, COUNT(*) AS number_of_shows
  FROM tv_genres as tg
       INNER JOIN tv_show_genres as tsg
       ON tg.id = tsg.genre_id
 GROUP BY tg.name
 ORDER BY number_of_shows DESC;
