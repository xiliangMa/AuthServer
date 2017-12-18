CREATE TABLE `UserNAS` (
  `Id` int NOT NULL,
  `Tel` bigint(30) NOT NULL,
  `NasId` char(255) NOT NULL,
  `isAdmin` BOOLEAN DEFAULT FALSE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`Tel`) REFERENCES `User` (`Tel`),
  FOREIGN KEY (`NasId`) REFERENCES `NASDevices` (`NasId`)
);