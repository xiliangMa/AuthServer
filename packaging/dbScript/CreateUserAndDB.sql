CREATE USER 'authserver'@'%' IDENTIFIED BY 'abc123';
GRANT ALL ON *.* TO 'authserver'@'%' IDENTIFIED BY 'abc123';
GRANT ALL ON *.* TO 'authserver'@'127.0.0.1' IDENTIFIED BY 'abc123';
CREATE DATABASE `authserver` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;