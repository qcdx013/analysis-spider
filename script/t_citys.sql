/*
Navicat MySQL Data Transfer

Source Server         : aws-rds
Source Server Version : 50627
Source Host           : awsdbinstance.c6pvm5chyyiq.ap-southeast-1.rds.amazonaws.com:3306
Source Database       : scrazz

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-03-05 12:01:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_citys
-- ----------------------------
DROP TABLE IF EXISTS `t_citys`;
CREATE TABLE `t_citys` (
  `province_id` varchar(64) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `province_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `province_first_letter` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city_id` varchar(64) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city_name` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `city_first_letter` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`city_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
