-- create view of students with scores under 80 who haven't had a meeting
-- in 80 days
CREATE VIEW need_meeting AS
    SELECT name FROM students
    WHERE score < 80 AND
    (ISNULL(last_meeting) OR DATEDIFF(NOW(), last_meeting) > 30);
