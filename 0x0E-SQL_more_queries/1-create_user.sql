-- A script that creates a user and assign privileges;

CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_pwd';
GRANT ALL PRIVILEGES ON mysql.database TO user_0d_1@localhost;
