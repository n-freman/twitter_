#!/bin/bash
set -e

psql -U postgres <<-EOSQL
	CREATE DATABASE twitter;
	CREATE USER twitteradmin WITH PASSWORD 'password123';
	GRANT ALL PRIVILEGES ON DATABASE twitter TO twitteradmin;
	ALTER DATABASE twitter SET OWNER TO twitteradmin;
EOSQL
