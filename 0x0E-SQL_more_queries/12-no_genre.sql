-- Lists all shows without a genre from the database hbtn_0d_tvshows
SELECT ts.title, tsg.genre_id
  FROM tv_shows AS ts
       LEFT JOIN tv_show_genres AS tsg
       ON ts.id = tsg.show_id
       WHERE tsg.show_id IS NULL
 ORDER BY ts.title, tsg.genre_id;
