SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Tel` bigint(30) NOT NULL,
  `Name` varchar(255) CHARACTER SET utf8,
  `Pwd` varchar(255) CHARACTER SET utf8 NOT NULL,
  `Email` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `SigKey` text CHARACTER SET utf8,
  `CreateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `LastLoginTime` timestamp NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`Tel`),
  KEY `Tel_User_index` (`Tel`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



-- ----------------------------
-- Table structure for ppdevices
-- ----------------------------
DROP TABLE IF EXISTS `ppdevices`;
CREATE TABLE `ppdevices` (
  `PPDeviceID` int(10) NOT NULL,
  `IsUsed` bigint(30),
  PRIMARY KEY (`PPDeviceID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for nasdevices
-- ----------------------------
DROP TABLE IF EXISTS `nasdevices`;
CREATE TABLE `nasdevices` (
  `NasId` bigint(30) NOT NULL,
  `IP` bigint(10),
  `MAC` varchar(255),
  PRIMARY KEY (`NasId`),
  KEY `NasId_NASDevices_index` (`NasId`) USING BTREE
) ENGINE=MyISAM DEFAULT CHARSET=utf8;



-- ----------------------------
-- Table structure for pshare
-- ----------------------------
DROP TABLE IF EXISTS `pshare`;
CREATE TABLE `pshare` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `NasId` bigint(30) NOT NULL,
  `ShareId` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Tel` bigint(30) DEFAULT NULL,
  `CreateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `HEAT` int(11) DEFAULT '0',
  PRIMARY KEY (`Id`),
  CONSTRAINT `NasId_PShare_FK` FOREIGN KEY (`NasId`) REFERENCES `nasdevices` (`NasId`),
  CONSTRAINT `Tel_PShare_FK` FOREIGN KEY (`Tel`) REFERENCES `user` (`Tel`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for usernas
-- ----------------------------
DROP TABLE IF EXISTS `usernas`;
CREATE TABLE `usernas` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Tel` bigint(30) NOT NULL,
  `NasId` varchar(255) NOT NULL,
  `IsAdmin` tinyint(1) DEFAULT FALSE,
  PRIMARY KEY (`Id`),
  KEY `Tel_UserNAS_index` (`Tel`) USING BTREE,
  CONSTRAINT `Tel_UserNAS_FK` FOREIGN KEY (`Tel`) REFERENCES `user` (`Tel`),
  CONSTRAINT `NasId_UserNAS_FK` FOREIGN KEY (`NasId`) REFERENCES `nasdevices` (`NasId`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


-- ----------------------------
-- Table structure for usersession
-- ----------------------------
DROP TABLE IF EXISTS `usersession`;
CREATE TABLE `usersession` (
  `Tel` bigint(30) NOT NULL,
  `RandomCode` int(10) NOT NULL,
  `CreateTime` timestamp DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Tel`),
  CONSTRAINT `Tel_UserSession_FK` FOREIGN KEY (`Tel`) REFERENCES `user` (`Tel`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

