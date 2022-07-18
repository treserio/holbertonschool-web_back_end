-- create an update trigger on users
-- reset valid_email to 0 if email changes
DELIMITER $$

CREATE TRIGGER reset_valid
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
    IF NOT NEW.email = OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$
