GRANT ALL PRIVILEGES ON *.* TO '${MYSQL_USER}'@'%' IDENTIFIED BY '${MYSQL_PASSWORD}' WITH GRANT OPTION;
FLUSH PRIVILEGES;
-- GRANT ALL PRIVILEGES ON *.* TO 'flask_user'@'%' IDENTIFIED BY 'flask_password' WITH GRANT OPTION;
-- FLUSH PRIVILEGES;