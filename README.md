KenshiDatabase-SQL
 
Description: KenshiDatabase is a database dedicated to sorting contents of the 2018 PC game Kenshi by Lo-Fi Games. The database is currently scoped to include the following 4 entity types: Zones(different areas of the map), Animals (non-human/shek/skeleton/hivers non-player-characters with their own variants and stats), Major Towns (large settlements of non-player-characters ruled by the games different factions), and Factions(the competing/collaborating organizations of non-player-characters within the game).

Table 1: zones
Desc: the many geographic regions of Kenshi
Table 1 PRIMARY KEY: zoneID(INTEGER)
Table 1 FOREIGN KEY: N/A
Table 1 attributes: zoneName(TEXT), environArid(FLOAT), environGreen(FLOAT), environSwamp(FLOAT)
zoneName: name of the zone
environArid: percentage that the zone is Arid
environGreen: percentage that the zone is Green
environSwamp: percentage that the zone is Swamp

Table 1 Current Columns:
(1, 'OkransPride', 0.0, 100.0, 0.0)
(2, 'TheSwamp', 0.0, 0.0, 100.0)
(3, 'StennDesert', 100.0, 0.0, 0.0)


Table 2: animals
Desc: the fauna(and machinery) of Kenshi
Table 2 PRIMARY KEY: animalID(INTEGER)
Table 2 FOREIGN KEY: fk_factionID(factionID)(factionID IN factions)
Table 2 attributes: name(TEXT), organicORrobot(TEXT), baseMelee(INTEGER), baseDefense(INTEGER)
name: name of the animal
organicORrobot: whether the animal is a robot or organic
baseMelee: all animals spawn with a random melee level within a set base range
baseDefense: all animals spawn with a random defense level within a set base range

Table 2 Current Columns:
(1, 'BeakThing', 'organic', 35, 35, NULL)
(2, 'Bonedog', 'organic', 20, 20, NULL)


Table 3: towns
Desc: the towns of Kenshi
Table 3 PRIMARY KEY: townID(INTEGER), townZoneID(INTEGER)
Table 3 FOREIGN KEY: townZoneID(INTEGER)(zoneID in zones), fk_townFactionID(townFactionID)(INTEGER)(factionID in factions)
Table 3 attributes: townname(TEXT), isMajor(BOOL), numBuilding(INTEGER), uniqueBuilding(TEXT)
townname: name of the town
isMajor: whether the town is considered to be a small or large settlement by the game
numBuilding: the number of buildings(including ruined or destroyed buildings) contained within the town
uniqueBuilding: named unique buildings contained within the town(if any)

Table 3 Current Columns:
(1, 'BadTeeth', 1, 1, 30, 1, NULL)
(2, 'Admag', 3, 1, 18, NULL, NULL)


Table 4: factions
Desc: the many factions of the world of Kenshi
Table 4 PRIMARY KEY: factionID(INTEGER)
Table 4 FOREIGN KEY: N/A
Table 4 attributes: factionName(TEXT), leaderName(TEXT), factionRace(TEXT), uniqueUnit(TEXT)
factionName: name of the faction
leaderName: name of the faction's leader (if any)
factionRace: dominant race of the faction(if any)
uniqueUnit: a character unit unique to that faction

Table 4 Current Columns:
(1, 'TheHolyNation', 'HolyLordPhoenix', 'Greenlander', 'Paladin'
(2, 'UnitedCities', 'EmperorTengu', 'Diverse', 'Samurai')


Table 5: spawn
Desc: bridge table to manage the many:many relationship between zones and animals, which zones spawn which animals
Table 4 PRIMARY KEY: spawnzoneID(INTEGER), spawnanimalID(INTEGER)
Table 4 FOREIGN KEY: spawnzoneID(INTEGER), spawnanimalID(INTEGER)
Table 5 Current Columns
(1, 2) #OkransPride contains Bonedog
(3, 2) #StennDesert contains Bonedog
