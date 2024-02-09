CREATE DATABASE twitter;
CREATE USER twitteradmin WITH PASSWORD 'password123';
GRANT ALL PRIVILEGES ON DATABASE twitter TO twitteradmin;
ALTER DATABASE twitter OWNER TO twitteradmin;
