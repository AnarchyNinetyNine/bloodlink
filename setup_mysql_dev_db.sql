-- Create database if not exists
CREATE DATABASE IF NOT EXISTS bloodlink_dev_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS "bloodlink_dev"@"localhost" IDENTIFIED BY "bloodlink_dev_pwd";

-- Grant priviledges
GRANT ALL ON bloodlink_dev_db.* TO "bloodlink_dev"@"localhost";
