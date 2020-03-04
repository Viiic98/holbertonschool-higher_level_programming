-- From an imported table
-- Display the shows that have at least one genre linked
SELECT tv_shows.title 'title', tv_show_genres.genre_id 'id'
FROM tv_show_genres
INNER JOIN tv_shows
      ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres
      ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, id ASC;
