-- Display genres
-- From a show name
SELECT tv_genres.name
FROM tv_genres 
INNER JOIN tv_show_genres 
      ON tv_show_genres.genre_id = tv_genres.id 
INNER JOIN tv_shows
      ON tv_shows.title = 'Dexter'
      AND tv_shows.id = tv_show_genres.show_id
ORDER BY tv_genres.name ASC;
