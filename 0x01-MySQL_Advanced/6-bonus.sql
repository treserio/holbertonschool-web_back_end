-- create a procedure that updates a user's score for a project if it exists
-- else add the project and update the user's score
DELIMITER ~~

DROP PROCEDURE IF EXISTS holberton.AddBonus;
CREATE PROCEDURE AddBonus(
    IN user_id int,
    IN project_name varchar(255),
    IN score int
)
BEGIN
    IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name) THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET @proj_id = LAST_INSERT_ID();
    ELSE
        SELECT @proj_id := id FROM projects WHERE name = project_name;
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, @proj_id, score);
END~~
