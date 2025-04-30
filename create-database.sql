-- DROP DATABASE IF EXISTS dalilah;

-- DROP ROLE IF EXISTS dalilah_admin;

CREATE DATABASE dalilah;

CREATE USER dalilah_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE dalilah TO dalilah_admin;