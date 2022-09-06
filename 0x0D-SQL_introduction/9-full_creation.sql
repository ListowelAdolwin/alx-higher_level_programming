-- Create a table, second_table
-- Insert data into the table
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT);

INSERT INTO second_table VALUES(id = 1, name = "John", score = 10);
INSERT INTO second_table VALUES(2, "Alex", 3);
INSERT INTO second_table VALUES(3, "Bob", 14);
INSERT INTO second_table VALUES(4, "George", 8);
