-- compute the average wheighted score for all students
DELIMITER ~~

DROP PROCEDURE IF EXISTS holberton.ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    JOIN corrections ON corrections.user_id = users.id
    JOIN projects ON projects.id = corrections.project_id
    SET average_score = (
        SELECT (SUM(projects.weight * corrections.score) / SUM(projects.weight))
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id
    );
END~~
