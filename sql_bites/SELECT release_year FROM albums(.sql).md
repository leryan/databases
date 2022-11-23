SELECT release_year FROM albums
    WHERE title = 'Bossanova';

UPDATE albums SET release_year = '1972' WHERE id = '3';

DELETE FROM albums WHERE id = '12';

-- We don't specify the value for the `id`
-- column, the database will automatically pick one.
INSERT INTO artists 
    (name, genre)
    VALUES('Massive Attack', 'Alternative');

INSERT INTO albums 
    (title, release_year)
    VALUES('Massive Attack', '1998');

UPDATE albums SET artist_id = '5' WHERE id = '13';