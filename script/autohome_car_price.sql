/*
Navicat MySQL Data Transfer

Source Server         : aws-rds
Source Server Version : 50627
Source Host           : awsdbinstance.c6pvm5chyyiq.ap-southeast-1.rds.amazonaws.com:3306
Source Database       : scrazz

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-03-05 12:02:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for autohome_car_price
-- ----------------------------
DROP TABLE IF EXISTS `autohome_car_price`;
CREATE TABLE `autohome_car_price` (
  `spec_id` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `city_id` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` float DEFAULT NULL,
  `price_min` float DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`spec_id`,`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
