-- Lists all genres of the show Dexter from the database hbtn_0d_tvshows
SELECT tg.name
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id
       WHERE tsg.show_id =
             (SELECT ts.id
	        FROM tv_shows AS ts
	       WHERE ts.title = 'Dexter')
 ORDER BY tg.name;
