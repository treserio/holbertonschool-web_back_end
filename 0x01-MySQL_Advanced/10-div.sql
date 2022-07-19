-- divide two numbers or returns 0 if the 2nd = 0
DELIMITER ~~

CREATE FUNCTION SafeDiv(a int, b int) RETURNS FLOAT
BEGIN
    IF b THEN
        RETURN a / b;
    END IF;
    RETURN 0;
END~~
