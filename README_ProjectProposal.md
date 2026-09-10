# KenshiDatabase-SQL
 
#Description: KenshiDatabase is a database dedicated to sorting contents of the 2018 PC game Kenshi by Lo-Fi Games. The database is currently scoped to include the following 4 entity types: Zones(different areas of the map), Animals (non-human/shek/skeleton/hivers non-player-characters with their own variants and stats), Major Towns (large settlements of non-player-characters ruled by the games different factions), and Factions(the competing/collaborating organizations of non-player-characters within the game).


#Use Cases: 
#Use Case 1: I would like to eventually use this database as a template for when I make my own game but adapted to my own needs.
#Use Case 2: The ability to organize and quickly receive the data for relevant and important game objects when encountering them or testing them would be useful.
#Use Case 3: Breaking down a game into organized data can bring new revelations about its design and allows for a holistic viewing of its contents.


#Entity Type 1: Zones
#Entity Type 1 Descriptions: EnvironmentArid, EnvironmentGreen, EnvironmentSwamp
#EnvironmentArid: percentage that the zone is Arid
#EnvironmentGreen: percentage that the zone is Green
#EnvironmentSwamp: percentage that the zone is Swamp

#Entity Type 1 List:
#Okran’s Pride – 0, 100, 0
#The Swamp – 0, 0, 100


#Entity Type 2: Animals
#Entity Type 2 Descriptions: OrganicOrRobot, BaseMeleeAtkLvl, Faction
#OrganicOrRobot: whether the animal is a robot or organic
#BaseMeleeAtkLvl: all animals spawn with a random attack level within a set base range
#Faction: all animals belong to a faction (generally specific to that single type of animal)

#Entity Type 2 List:
#Beak Thing – Organic, 35, Gutters
#Bonedog – Organic, 20, Wolves


#Entity Type 3: MajorTowns
#Entity Type 3 Descriptions: OwnerFaction, ZoneLocation, UniqueBuilding
#OwnerFaction: which faction owns the town
#ZoneLocation: which zone is the town in
#UniqueBuilding: a unique building to that town(if that town has one)

#Entity Type 3 List:
#Bad Teeth – TheHolyNation, OkransPride, NA
#Admag – ShekKingdom, StennDesert, FactionHQ


#Entity Type 4: Faction
#Entity Type 4 Descriptions: FactionHQ, FactionLeader, FactionRace
#FactionHQ: where a faction's main base is, generally within a major town
#FactionLeader: which NPC is the faction's leader
#FactionRace: dominant NPC race of the faction(if any)

#Entity Type 4 List:
#The Holy Nation – BlisterHill, HolyLordPhoenix, Greenlander
#United Cities – Heft, EmperorTengu, Multi
