-- create a procedure that updates a user's score for a project if it exists
-- else add the project and update the user's score
DELIMITER ~~

DROP PROCEDURE IF EXISTS holberton.ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id int)
BEGIN
    SET @st_avg = (SELECT AVG(score) FROM corrections
        WHERE corrections.user_id = user_id
    );
    UPDATE users
    SET average_score = @st_avg
    WHERE id = user_id;
END~~
