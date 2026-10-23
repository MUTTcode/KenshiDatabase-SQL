#zone-animals Many:Many
import os
import mysql.connector, json

with open('secrets.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

connection = mysql.connector.connect(**creds)

print(connection)
connection.close()


def printTableZones():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM zones;")
    myresult = mycursor.fetchall()

    print(f"\n{'zoneID':>4}  {'zoneName':<30} {'environArid':<6} {'environGreen':<6} {'environSwamp':<6}")
    print("-" * 56)
    for zoneID, zoneName, environArid, environGreen, environSwamp in myresult:
        print(f"{zoneID:>4}  {zoneName:<30} {environArid:<6} {environGreen:<6} {environSwamp:<6} ")
    while myresult is not None:
        print(myresult)
        break

    connection.close()


def printTableAnimals():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM animals;")
    myresult = mycursor.fetchall()

    print(f"\n{'animalID':>4}  {'name':<30} {'organicORrobot':<10} {'baseMelee':<6} {'baseDefense':<6} {'factionID':<6}")
    print("-" * 66)
    for animalID, name, organicORrobot, baseMelee, baseDefense, factionID in myresult:
        print(f"{animalID:>4}  {name:<30} {organicORrobot:<10} {baseMelee:<6} {baseDefense:<6} {factionID:<6}")
    while myresult is not None:
        print(myresult)
        break

    connection.close()


def printZonesAndAnimals():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    mycursor.execute(
    "SELECT zoneName, name FROM zones LEFT JOIN spawn ON (zones.zoneID=spawnzoneID) LEFT JOIN animals ON (animals.animalID=spawnanimalID);"
    )
    
    myresult_zonesandanimals = mycursor.fetchall()
    print(f"\n{myresult_zonesandanimals}")
    
    connection.close()


def printZonesForAnimal():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    animalID = input(
        f"For which animalID would you"
        f" like to view the zones? "
        )
    
    mycursor.execute("SELECT zones.zoneID, zoneName FROM zones JOIN spawn ON zones.zoneID=spawn.spawnzoneID WHERE spawnanimalID=%s;", (animalID,))
    myresult = mycursor.fetchall()
    mycursor.execute("SELECT animals.name FROM animals WHERE animalID=%s;", (animalID,))
    myresult_name = mycursor.fetchone()

    print(f"There are {len(myresult)} zone(s) containing {myresult_name}: ")
    for row in myresult:
        print(row)
    
    connection.close()


def printAnimalsInZone():
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    zoneID = input(
        f"For which zoneID would you like to" 
        f" view contained animals?: "
        )
    mycursor.execute("SELECT animals.animalID, name FROM animals JOIN spawn ON animals.animalID=spawn.spawnanimalID WHERE spawnzoneID=%s;", (zoneID,))
    myresult = mycursor.fetchall()
    mycursor.execute("SELECT zones.zoneName FROM zones WHERE zoneID=%s;", (zoneID,))
    myresult_name = mycursor.fetchone()

    print(f"There are {len(myresult)} animal(s) within the zone {myresult_name}: ")
    
    for row in myresult:
        print(row)
    
    connection.close()


def addAnimalIntoZone():
    zoneID = input("Please give the ID of the zone\n"
    "you wish to add an animal to: ")
    animalID = input(
        f"Please give the ID of the animal you wish\n" 
        f"to add to zone {zoneID}: ")

    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    mycursor.execute( 
        "SELECT zoneName FROM zones WHERE zoneID=%s", (zoneID,))
    myresult_zonename = mycursor.fetchone()
    mycursor.execute( 
        "SELECT name FROM animals WHERE animalID=%s", (animalID,))
    myresult_animalname = mycursor.fetchone()

    add_animalintozone_yn = input(
        f"Do you wish to add animal: {myresult_animalname}" 
        f"into zone: {myresult_zonename}?\n"
        f"(y/n): ").strip().lower()
    while add_animalintozone_yn not in ("y", "yes"):
        print("Cancelled.\n")
        break            
    
    mycursor.execute(
        "INSERT INTO spawn(spawnzoneID, spawnanimalID)"
        "VALUES (%s, %s);",
        (zoneID, animalID)
    )
    
    connection.commit()
    connection.close()


def deleteAnimalFromZone():
    animalID = input(f"Please give the ID of the animal"
    f" you wish to remove from a zone: "
    )
    zoneID = input(
        f"Please give the ID of the zone you wish" 
        f" to remove animal {animalID} from: ")

    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    mycursor.execute( 
        "SELECT name FROM animals WHERE animalID=%s", (animalID,))
    myresult_animalname = mycursor.fetchone()
    mycursor.execute( 
        "SELECT zoneName FROM zones WHERE zoneID=%s", (zoneID,))
    myresult_zonename = mycursor.fetchone()

    del_animalfromzone_yn = input(
        f"Do you really want to remove animal: {myresult_animalname}" 
        f"from zone: {myresult_zonename}?\n"
        f"(y/n): ").strip().lower()
    while del_animalfromzone_yn not in ("y", "yes"):
        print("Cancelled.\n")
        break            
    
    mycursor.execute(
        "DELETE FROM spawn WHERE spawnzoneID=%s AND spawnanimalID=%s;",
        (zoneID, animalID)
    )
    
    connection.commit()
    connection.close()


menuText = """Please select one of the following options:
1) Display zones
2) Display animals
3) Print all zones and associated animals
4) Print zones where you can find an animal
5) Print animals found in a zone
6) Add an animal to a zone
7) Delete an animal from a zone
q) Quit
"""

if __name__ == "__main__":
    while True:
        choice = input(menuText)
        if choice == "q":
            break
        elif choice == "1":
            printTableZones()
        elif choice == "2":
            printTableAnimals()
        elif choice == "3":
            printZonesAndAnimals()
        elif choice == "4":
            printZonesForAnimal()
        elif choice == "5":
            printAnimalsInZone()
        elif choice == "6":
            addAnimalIntoZone()
        elif choice == "7":
            deleteAnimalFromZone()

        else:
            print("That is not a valid choice.")
            print(menuText)




