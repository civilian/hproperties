/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
ALTER TABLE `property`
ADD `last_status_history` int;
ALTER TABLE `property`
ADD CONSTRAINT `last_status_history_fk` FOREIGN KEY (`last_status_history`) REFERENCES `status_history` (`id`);
/*!40101 SET character_set_client = @saved_cs_client */;