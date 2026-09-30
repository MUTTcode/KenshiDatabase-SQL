-- MySQL dump 10.13  Distrib 8.4.11, for Linux (x86_64)
--
-- Host: localhost    Database: KENSHI
-- ------------------------------------------------------
-- Server version	8.4.11-0ubuntu0.26.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `animals`
--

DROP TABLE IF EXISTS `animals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animals` (
  `animalID` int NOT NULL,
  `name` text,
  `organicORrobot` text,
  `baseMelee` int DEFAULT NULL,
  `baseDefense` int DEFAULT NULL,
  `factionID` int DEFAULT NULL,
  PRIMARY KEY (`animalID`),
  KEY `fk_factionID` (`factionID`),
  CONSTRAINT `fk_factionID` FOREIGN KEY (`factionID`) REFERENCES `factions` (`factionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animals`
--

LOCK TABLES `animals` WRITE;
/*!40000 ALTER TABLE `animals` DISABLE KEYS */;
INSERT INTO `animals` VALUES (1,'BeakThing','organic',35,35,NULL),(2,'Bonedog','organic',20,20,NULL);
/*!40000 ALTER TABLE `animals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `factions`
--

DROP TABLE IF EXISTS `factions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `factions` (
  `factionName` text,
  `factionID` int NOT NULL,
  `leaderName` text,
  `factionRace` text,
  `uniqueUnit` text,
  PRIMARY KEY (`factionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `factions`
--

LOCK TABLES `factions` WRITE;
/*!40000 ALTER TABLE `factions` DISABLE KEYS */;
INSERT INTO `factions` VALUES ('TheHolyNation',1,'HolyLordPhoenix','Greenlander','Paladin'),('UnitedCities',2,'EmperorTengu','Diverse','Samurai');
/*!40000 ALTER TABLE `factions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spawns`
--

DROP TABLE IF EXISTS `spawns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spawns` (
  `spawnzoneID` int DEFAULT NULL,
  `spawnanimalID` int DEFAULT NULL,
  `animalName` text,
  `zoneName` text,
  KEY `spawnzoneID` (`spawnzoneID`),
  KEY `spawnanimalID` (`spawnanimalID`),
  CONSTRAINT `spawns_ibfk_1` FOREIGN KEY (`spawnzoneID`) REFERENCES `zones` (`zoneID`),
  CONSTRAINT `spawns_ibfk_2` FOREIGN KEY (`spawnanimalID`) REFERENCES `animals` (`animalID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spawns`
--

LOCK TABLES `spawns` WRITE;
/*!40000 ALTER TABLE `spawns` DISABLE KEYS */;
INSERT INTO `spawns` VALUES (NULL,1,'BeakThing',NULL),(NULL,2,'Bonedog',NULL),(1,NULL,NULL,'OkransPride'),(2,NULL,NULL,'TheSwamp');
/*!40000 ALTER TABLE `spawns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `towns`
--

DROP TABLE IF EXISTS `towns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `towns` (
  `townname` text,
  `townZoneID` int DEFAULT NULL,
  `townZone` text,
  `isMajor` tinyint(1) DEFAULT NULL,
  `numBuilding` int DEFAULT NULL,
  `townFaction` text,
  `townFactionID` int DEFAULT NULL,
  `uniqueBuilding` text,
  KEY `townZoneID` (`townZoneID`),
  KEY `fk_townFactionID` (`townFactionID`),
  CONSTRAINT `fk_townFactionID` FOREIGN KEY (`townFactionID`) REFERENCES `factions` (`factionID`),
  CONSTRAINT `towns_ibfk_1` FOREIGN KEY (`townZoneID`) REFERENCES `zones` (`zoneID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `towns`
--

LOCK TABLES `towns` WRITE;
/*!40000 ALTER TABLE `towns` DISABLE KEYS */;
INSERT INTO `towns` VALUES ('BadTeeth',1,'OkransPride',1,30,'TheHolyNation',1,NULL),('Admag',NULL,'StennDesert',1,18,'ShekKingdom',NULL,NULL);
/*!40000 ALTER TABLE `towns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zones`
--

DROP TABLE IF EXISTS `zones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zones` (
  `zoneID` int NOT NULL,
  `zoneName` text,
  `environArid` float DEFAULT NULL,
  `environGreen` float DEFAULT NULL,
  `environSwamp` float DEFAULT NULL,
  PRIMARY KEY (`zoneID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zones`
--

LOCK TABLES `zones` WRITE;
/*!40000 ALTER TABLE `zones` DISABLE KEYS */;
INSERT INTO `zones` VALUES (1,'OkransPride',0,100,0),(2,'TheSwamp',0,0,100);
/*!40000 ALTER TABLE `zones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-09-30 11:01:15
