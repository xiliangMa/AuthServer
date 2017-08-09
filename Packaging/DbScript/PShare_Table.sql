CREATE TABLE `PShare` (
  `Id` int NOT NULL,
  `NasId` char(255) NOT NULL,
  `ShareId` int NOT NULL,
  `Name` char(255) DEFAULT null,
  `Tel` bigint(30),
  `CreateTime` TIMESTAMP,
  `HEAT` int DEFAULT 0,
  PRIMARY KEY (`Id`),
  FOREIGN KEY (`NasId`) REFERENCES `NASDevices` (`NasId`),
  FOREIGN KEY (`Tel`) REFERENCES `Users` (`Tel`)
);