-- compute the average wheighted score for a student
DELIMITER ~~

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    FOR EACH ROW id IN users
        ComputeAverageWeightedScoreForUser(id);
END~~
