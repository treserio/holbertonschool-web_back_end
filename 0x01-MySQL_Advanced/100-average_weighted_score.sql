-- compute the average wheighted score for a student
DELIMITER ~~

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    UPDATE users
    SET average_score = (
        SELECT (SUM(projects.weight * corrections.score) / SUM(projects.weight))
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id
    )
    WHERE users.id = user_id;
END~~
