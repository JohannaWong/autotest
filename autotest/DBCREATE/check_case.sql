/*清空三个表，并将def中添加all，产品线添加到productline表中*/
truncate table productline;
truncate table cases;
truncate table def;
INSERT INTO `def` VALUES (1,'ALL',NULL);
INSERT INTO `productline` VALUES (1,'luckywin','http://slots-team-test-new.tuanguwen.com:7310/SlotServer/tpanel');
INSERT INTO `productline` VALUES (2,'simvegas','http://123.57.55.85:7001/tpanel');
INSERT INTO `productline` VALUES (3,'Double_x','http://52.70.128.131:9940/tPanel');