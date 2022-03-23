--
-- Table structure for table `status_history`
--

DROP TABLE IF EXISTS `social_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_like` (
  `id` int NOT NULL AUTO_INCREMENT,
  `property_id` int NOT NULL,
  `auth_user_id` int NOT NULL,
  `social_like` tinyint(1) NOT NULL,
  `update_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_like_id_uindex` (`id`),
  KEY `social_like_property_id_fk` (`property_id`),
  KEY `social_like_auth_user_id_fk` (`auth_user_id`),
  CONSTRAINT `social_like_property_id_fk` FOREIGN KEY (`property_id`) REFERENCES `property` (`id`),
  CONSTRAINT `social_like_status_id_fk` FOREIGN KEY (`auth_user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;