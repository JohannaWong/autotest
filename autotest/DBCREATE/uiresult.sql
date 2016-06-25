/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50528
Source Host           : localhost:3306
Source Database       : slot

Target Server Type    : MYSQL
Target Server Version : 50528
File Encoding         : 65001

Date: 2016-06-25 21:04:33
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `uiresult`
-- ----------------------------
DROP TABLE IF EXISTS `uiresult`;
CREATE TABLE `uiresult` (
  `id` int(40) NOT NULL AUTO_INCREMENT,
  `runtime` varchar(225) DEFAULT NULL,
  `passnum` int(40) DEFAULT NULL,
  `failnum` int(40) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of uiresult
-- ----------------------------
INSERT INTO `uiresult` VALUES ('1', '3.5s', '1', '0', 'uitest001.log');
INSERT INTO `uiresult` VALUES ('2', '155.986s', '1', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625201605.txt');
INSERT INTO `uiresult` VALUES ('3', '155.5s', '2', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625202307.txt');
INSERT INTO `uiresult` VALUES ('4', '113.721s', '1', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625202737.txt');
INSERT INTO `uiresult` VALUES ('5', '155.49s', '2', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625203211.txt');
INSERT INTO `uiresult` VALUES ('6', '136.705s', '3', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625204002.txt');
INSERT INTO `uiresult` VALUES ('7', '157.271s', '4', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625204558.txt');
INSERT INTO `uiresult` VALUES ('8', '112.755s', '1', '0', '..\\\\Web\\\\logs\\\\uitestlog20160625210053.txt');
