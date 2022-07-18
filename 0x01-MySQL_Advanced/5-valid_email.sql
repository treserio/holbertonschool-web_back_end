-- create an update trigger on users
-- reset valid_email to 0 if email changes

CREATE TRIGGER reset_valid
BEFORE UPDATE ON users FOR EACH ROW
    IF NEW.id == OLD.id
        SET valid_email = 0;
