-- Lists all shows from the database
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_shows ts
        JOIN tv_show_ratings tsr
	     ON ts.id = tsr.show_id
GROUP BY ts.id
ORDER BY rating DESC;
