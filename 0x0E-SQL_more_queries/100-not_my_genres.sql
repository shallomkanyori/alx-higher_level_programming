-- Lists all genres not lined to the show Dexter from the database
-- hbtn_0d_tvshows
SELECT tg.name
  FROM tv_genres AS tg
 WHERE tg.id NOT IN
       (SELECT tsg.genre_id
	  FROM tv_show_genres AS tsg
	       INNER JOIN tv_shows AS ts
	       ON tsg.show_id = ts.id
	       WHERE ts.title = 'Dexter')
 ORDER BY tg.name;
