-- create an update trigger on users
-- reset valid_email to 0 if email changes

CREATE TRIGGER reset_valid
AFTER UPDATE ON users FOR EACH ROW
    IF NEW.email == email
        SET valid_email = 0;
