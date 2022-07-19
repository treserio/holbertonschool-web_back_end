-- create an index of the first letter of the name field of names and score
CREATE INDEX idx_name_first ON names (name(1), score);
