/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50528
Source Host           : localhost:3306
Source Database       : slot

Target Server Type    : MYSQL
Target Server Version : 50528
File Encoding         : 65001

Date: 2016-06-16 01:33:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `stress_tasks`
-- ----------------------------
DROP TABLE IF EXISTS `stress_tasks`;
CREATE TABLE `stress_tasks` (
  `id` bigint(30) NOT NULL AUTO_INCREMENT,
  `scriptname` varchar(255) DEFAULT NULL,
  `threadnum` varchar(255) DEFAULT NULL,
  `averagetime` varchar(255) DEFAULT NULL,
  `totaltime` varchar(255) DEFAULT NULL,
  `errors` bigint(40) DEFAULT NULL,
  `exec_set` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stress_tasks
-- ----------------------------
INSERT INTO `stress_tasks` VALUES ('1', '1', '5', '0.003', '3.332', '0', '运行次数:1', null);
INSERT INTO `stress_tasks` VALUES ('2', '1', '6', '0.002', '2.109', '0', '运行次数:2', null);
INSERT INTO `stress_tasks` VALUES ('3', '1', '6', '0.002', '1.522', '0', '运行次数:2', null);
INSERT INTO `stress_tasks` VALUES ('4', '1', '4', '0.002', '4.523', '0', '运行次数:3', null);
INSERT INTO `stress_tasks` VALUES ('5', '1', '4', '0.002', '1.669', '0', '运行次数:3', null);
INSERT INTO `stress_tasks` VALUES ('6', '1', '4', '0.002', '1.739', '0', '运行次数:3', null);
