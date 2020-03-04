-- From an imported table
-- Display the shows that have at least one genre linked
SELECT tv_shows.title 'title', tv_show_genres.genre_id 'id'
FROM tv_shows, tv_show_genres 
WHERE tv_show_genres.show_id = tv_shows.id
ORDER BY title, id ASC;
