-- creates table called 'first_table' if it exists it shouldn't fail
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
