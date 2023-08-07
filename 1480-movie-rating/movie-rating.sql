# Write your MySQL query statement below
WITH UserRatings AS (
    SELECT u.name AS user_name, 
           COUNT(*) AS rated_movies,
           ROW_NUMBER() OVER (ORDER BY COUNT(*) DESC, u.name ASC) AS user_rank
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.name
),
MovieAvgRatings AS (
    SELECT m.title AS movie_title, 
           AVG(mr.rating) AS avg_rating,
           ROW_NUMBER() OVER (ORDER BY AVG(mr.rating) DESC, m.title ASC) AS movie_rank
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE DATE_FORMAT(mr.created_at, '%Y-%m') = '2020-02'
    GROUP BY m.title
)
SELECT user_name AS results
FROM UserRatings
WHERE user_rank = 1
UNION ALL
SELECT movie_title AS results
FROM MovieAvgRatings
WHERE movie_rank = 1;
