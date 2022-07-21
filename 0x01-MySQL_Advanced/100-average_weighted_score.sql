-- compute the average wheighted score for a student
DELIMITER ~~

CREATE FUNCTION ComputeAverageWeightedScoreForUser(user_id int) RETURNS VOID
BEGIN
    SET @total = SELECT SUM(projects.weight * corrections.score) from corrections
    INNER JOIN projects on corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    UPDATE users
    SET average_score = @total
    WHERE users.id = user_id;
END~~
