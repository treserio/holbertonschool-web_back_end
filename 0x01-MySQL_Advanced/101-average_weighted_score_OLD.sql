-- compute the average wheighted score for all students
DELIMITER ~~

DROP PROCEDURE IF EXISTS holberton.ComputeAverageWeightedScoreForUser;
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

DROP PROCEDURE IF EXISTS holberton.ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    SET @CustID = 0;
    SET @RUN_LOOP = 1;
    WHILE @RUN_LOOP DO
        SET @CustID = (SELECT id FROM users
            WHERE id > @CustID
            ORDER BY id
            LIMIT 1
        );

        SET @RUN_LOOP = FOUND_ROWS();

        CALL ComputeAverageWeightedScoreForUser(@CustID);
    END WHILE;
END~~
