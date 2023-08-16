-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tg.name, SUM(tsr.rate) AS rating
  FROM tv_genres AS tg
       LEFT JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id
       LEFT JOIN tv_show_rating AS tsr
       ON tsg.show_id = tsr.show_id
 GROUP BY tg.name
 ORDER BY rating DESC;
