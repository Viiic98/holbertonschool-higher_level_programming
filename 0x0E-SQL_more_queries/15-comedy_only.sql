-- SEARCH IN A DB
-- The Comedy shows
SELECT tv_shows.title
FROM tv_show_genres
INNER JOIN tv_genres
      ON tv_genres.name = 'Comedy'
      AND tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
      ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title;
