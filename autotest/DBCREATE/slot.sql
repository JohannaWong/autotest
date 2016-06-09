# MySQL-Front 5.1  (Build 4.13)

/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE */;
/*!40101 SET SQL_MODE='' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES */;
/*!40103 SET SQL_NOTES='ON' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;


# Host: 127.0.0.1    Database: slot
# ------------------------------------------------------
# Server version 5.0.45-community-nt

#
# Source for table cases
#

DROP TABLE IF EXISTS `cases`;
CREATE TABLE `cases` (
  `caseid` int(4) NOT NULL auto_increment,
  `casename` varchar(40) default NULL,
  `productid` int(4) default NULL,
  PRIMARY KEY  (`caseid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

#
# Dumping data for table cases
#
truncate table cases;

LOCK TABLES `cases` WRITE;
/*!40000 ALTER TABLE `cases` DISABLE KEYS */;
INSERT INTO `cases` VALUES (2,'test_Forest_Mania',1);
INSERT INTO `cases` VALUES (3,'test_Grand_win',1);
INSERT INTO `cases` VALUES (4,'test_lucky_star',1);
INSERT INTO `cases` VALUES (5,'test_Rapid_Hit',1);
INSERT INTO `cases` VALUES (6,'test_super_777',1);
INSERT INTO `cases` VALUES (7,'test1',2);
INSERT INTO `cases` VALUES (8,'test2',2);
INSERT INTO `cases` VALUES (9,'test_gold_wild',1);
INSERT INTO `cases` VALUES (12,'test_Fire_born',3);
INSERT INTO `cases` VALUES (13,'test_lucky_star',9);
INSERT INTO `cases` VALUES (14,'test_Super_winner',3);
INSERT INTO `cases` VALUES (15,'test_Wolf_Moon',3);
/*!40000 ALTER TABLE `cases` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table def
#

DROP TABLE IF EXISTS `def`;
CREATE TABLE `def` (
  `defid` int(4) NOT NULL auto_increment,
  `defname` varchar(40) default NULL COMMENT '方法的名称',
  `caseid` int(4) default NULL COMMENT '用例ID',
  PRIMARY KEY  (`defid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table def
#
truncate table def;

LOCK TABLES `def` WRITE;
/*!40000 ALTER TABLE `def` DISABLE KEYS */;
INSERT INTO `def` VALUES (1,'ALL',NULL);
INSERT INTO `def` VALUES (2,'test_Forest_Mania',2);
INSERT INTO `def` VALUES (3,'test_252',3);
INSERT INTO `def` VALUES (4,'test_777',3);
INSERT INTO `def` VALUES (5,'test_7bar',3);
INSERT INTO `def` VALUES (6,'test_other',3);
INSERT INTO `def` VALUES (7,'test_red7',4);
INSERT INTO `def` VALUES (8,'test_zi7',4);
INSERT INTO `def` VALUES (9,'test_blue7',4);
INSERT INTO `def` VALUES (10,'test_7bar',4);
INSERT INTO `def` VALUES (11,'test_blue7',4);
INSERT INTO `def` VALUES (12,'test_blue7_bar_blue7',4);
INSERT INTO `def` VALUES (13,'test_blue7_bar_blue7_no',4);
INSERT INTO `def` VALUES (14,'test_any7',4);
INSERT INTO `def` VALUES (15,'test_red7_red7',4);
INSERT INTO `def` VALUES (16,'test_7bar_3bar_2bar',4);
INSERT INTO `def` VALUES (17,'test_7bar_3bar_2bar',4);
INSERT INTO `def` VALUES (20,'test_Rapid_Hit',5);
INSERT INTO `def` VALUES (21,'wild5',5);
INSERT INTO `def` VALUES (23,'test_7',9);
INSERT INTO `def` VALUES (26,'test_bar',9);
INSERT INTO `def` VALUES (27,'test_wild',9);
INSERT INTO `def` VALUES (28,'test_7_wild',9);
/*!40000 ALTER TABLE `def` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table productline
#

DROP TABLE IF EXISTS `productline`;
CREATE TABLE `productline` (
  `id` int(4) NOT NULL auto_increment,
  `productline_name` varchar(20) default NULL COMMENT '产品线名称',
  `productline_url` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table productline
#
truncate table productline;

LOCK TABLES `productline` WRITE;
/*!40000 ALTER TABLE `productline` DISABLE KEYS */;
INSERT INTO `productline` VALUES (1,'luckywin','http://slots-team-test-new.tuanguwen.com:7310/SlotServer/tpanel');
INSERT INTO `productline` VALUES (2,'simvegas','http://123.57.55.85:7001/tpanel');
INSERT INTO `productline` VALUES (3,'Double_x','http://52.70.128.131:9940/tPanel');
/*!40000 ALTER TABLE `productline` ENABLE KEYS */;
UNLOCK TABLES;

#
# Source for table tasks
#

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `taskid` int(10) NOT NULL auto_increment COMMENT '执行的任务id',
  `playerid` int(11) default NULL,
  `productid` int(4) default NULL COMMENT '产品线id',
  `caseid` int(10) default NULL COMMENT '用例id',
  `defid` int(10) default NULL COMMENT '方法id',
  `addtime` timestamp NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '添加时间',
  `result` varchar(40) default NULL COMMENT '返回结果',
  PRIMARY KEY  (`taskid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Dumping data for table tasks
#
truncate table tasks;

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES (1,1,1,1,1,'2016-05-31 23:17:55','pass');
INSERT INTO `tasks` VALUES (2,89098,1,3,2,NULL,'{\"result\":\"ok\"}');
INSERT INTO `tasks` VALUES (3,1234321,1,3,2,NULL,'{\"result\":\"ok\"}');
INSERT INTO `tasks` VALUES (4,89876565,1,2,0,NULL,'{\"result\":\"ok\"}');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
