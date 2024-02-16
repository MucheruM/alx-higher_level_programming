-- Lists all genres in the database and their ratings
SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_genres tg
        JOIN tv_shows_genres tsg
	        ON tg.id = tsg.genre_id
	JOIN tv_show_ratings tsr
	        ON tsg.show_id = tsr.show_id
GROUP BY tg.id
ORDER BY rating DESC;
