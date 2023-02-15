/*
A script that creates the  database 'hbtn_0d_2' and the user 'user_0d_2'

With the following conditions:
	user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
	he user_0d_2 password should be set to user_0d_2_pwd
	f the database hbtn_0d_2 already exists, your script should not fail
	ifhe user user_0d_2 already exists, your script should not fail
*/

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* to user_0d_2@localhost;
