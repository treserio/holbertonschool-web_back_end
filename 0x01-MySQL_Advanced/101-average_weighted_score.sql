-- compute the average wheighted score for a student
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
    lp: WHILE TRUE DO
        SET @CustID = (SELECT id FROM users
            WHERE id > @CustID
            ORDER BY id
            LIMIT 1
        );

        IF FOUND_ROWS() = 0 THEN
            LEAVE lp;
        END IF;

        CALL ComputeAverageWeightedScoreForUser(@CustID);
    END WHILE;
END~~
