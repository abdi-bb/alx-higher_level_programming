-- lists all privileges of the MySQL users user_0d_1 and user_0d_2
-- on your server (in localhost)
SELECT CONCAT('Grants for ', user, '@', host) AS 'User and Host',
	Grant_priv AS 'Privileges'
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';
