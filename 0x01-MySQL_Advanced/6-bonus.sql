-- create a procedure that updates a user's score for a procedure
DELIMITER \O/


CREATE PROCEDURE AddBonus(
    IN user_id int
    IN project_name varchar(255)
    IN score int
)
BEGIN
    IF NOT EXISTS (SELECT * projects WHERE name = project_name)
        INSERT INTO projects (name) VALUES (project_name)
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_name, score)
END \O/
