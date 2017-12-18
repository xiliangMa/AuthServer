CREATE TABLE `User` (
  `Tel` bigint(30) NOT NULL,
  `Name` char(255) NOT NULL,
  `Pwd` char(255) NOT NULL,
  `Email` char(255) DEFAULT NULL,
  `SigKey` TEXT,
  `CreateTime` TIMESTAMP,
  `LastLoginTime` TIMESTAMP,
  PRIMARY KEY (`tel`)
);