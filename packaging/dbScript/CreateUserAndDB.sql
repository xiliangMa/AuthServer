CREATE USER 'authserver'@'%' IDENTIFIED BY 'abc123';
GRANT ALL ON *.* TO 'authserver'@'%';
CREATE DATABASE `authserver` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;