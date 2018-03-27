CREATE USER 'authserver'@'%' IDENTIFIED BY 'P@ssw0rd';
-- loca test remote conn
--GRANT ALL ON *.* TO 'authserver'@'%' IDENTIFIED BY 'abc123';
GRANT ALL ON *.* TO 'authserver'@'127.0.0.1' IDENTIFIED BY 'P@ssw0rd';
CREATE DATABASE `authserver` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;