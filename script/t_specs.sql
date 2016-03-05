/*
Navicat MySQL Data Transfer

Source Server         : aws-rds
Source Server Version : 50627
Source Host           : awsdbinstance.c6pvm5chyyiq.ap-southeast-1.rds.amazonaws.com:3306
Source Database       : scrazz

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-03-05 12:01:41
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_specs
-- ----------------------------
DROP TABLE IF EXISTS `t_specs`;
CREATE TABLE `t_specs` (
  `brand_id` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `brand_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `brand_img_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `series_id` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `series_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  `series_img_url` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `spec_id` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `spec_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`spec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
