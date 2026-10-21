#zoneMenu
import os
import mysql.connector, json

with open('secrets.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

connection = mysql.connector.connect(**creds)

print(connection)
connection.close()

def askId(prompt):
    while True:
        answer = input(prompt).strip()
        if answer.isdigit():
            return int(answer)
        print("Please enter a whole number.")


def askFloat(prompt, current=None):
    while True:
        label = f"{prompt} [{current}]: " if current is not None else f"{prompt}: "
        answer = input(label).strip()
        if answer:
            return answer
        if current is not None:
            return current
        print("This field can't be blank.")


def askInteger(prompt, current=None):
    while True:
        label = f"{prompt} [{current}]: " if current is not None else f"{prompt}: "
        answer = input(label).strip()
        if answer:
            return answer
        if current is not None:
            return current
        print("This field can't be blank.")


def askText(prompt, current=None):
    while True:
        label = f"{prompt} [{current}]: " if current is not None else f"{prompt}: "
        answer = input(label).strip()
        if answer:
            return answer
        if current is not None:
            return current
        print("This field can't be blank.")


""" def fetchRow(cursor, zoneID):
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    mycursor.execute(
        "SELECT zoneID, zoneName, environArid, environGreen, environSwamp "
        "FROM zones WHERE zoneID=%s;",
        (zoneID),
    )
    
    mycursor.execute

    return myresult """


def printTable():
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


def insertIntoTable():
    zoneName = askText("Please give the name of the zone")
    environArid = askFloat("Please give the percentage the zone's environment is Arid")
    environGreen = askFloat("Please give the percentage the zone's environment is Green")
    environSwamp = askFloat("Please give the percentage the zone's environment is Swamp")

    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    mycursor.execute( 
        "INSERT INTO zones (zoneName, environArid, environGreen, environSwamp)"
        "VALUES (%s, %s, %s, %s);",
        (zoneName, environArid, environGreen, environSwamp),
    )
    connection.commit()
    mycursor.execute

    connection.close()


def updateRow():
    zoneID = askId("What is the id of the zone you want to update? ")
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM zones WHERE zoneID=%s", (zoneID,))
    myresult = mycursor.fetchone()
    print(f"The current row has the value: {myresult}")
    print("Press Enter to keep a value unchanged.")
    
    zoneName = input("Enter the new name of the zone: ")
    environArid = input("Enter the new arid environmental percent of the zone: ")
    environGreen = input("Enter the new green environmental percent of the zone: ")
    environSwamp = input("Enter the new swamp environmental percent of the zone: ")
    mycursor.execute("UPDATE zones SET zoneName=%s, environArid=%s, environGreen=%s, environSwamp=%s WHERE zoneID=%s;",
        (zoneName, environArid, environGreen, environSwamp, zoneID)
    )
    connection.commit()
    print(f"Updated zone: {zoneName} zoneID: {zoneID}.\n")
    
    connection.close()


def deleteRowFromTable():
    zoneID = input("What is the ID of the zone to delete? ")
    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()
    
    mycursor.execute("SELECT * FROM zones WHERE zoneID=%s", (zoneID,))
    myresult = mycursor.fetchone()
    

    
    while zoneID is None:
        print(f"No zone with ID {zoneID}.\n")
        print("Cancelling.")
        break

    delete_zone_yn= input(f"Delete zone: {zoneID}? (y/n): ").strip().lower()
    while delete_zone_yn not in ("y", "yes"):
        print("Cancelled.\n")
        break

    try:
        mycursor.execute("DELETE FROM zones WHERE zoneID=%s", (zoneID,))
        connection.commit()
        print(f"Deleted zone {zoneID}.\n")
    except mysql.connector.IntegrityError as err:
        connection.rollback()
        if err.errno == errorcode.ER_ROW_IS_REFERENCED_2:
            print(
                "Can't delete: this zone is still used in spawn "
                "or towns. Remove those rows first.\n")
    connection.commit()
    connection.close()   


menuText = """Please select one of the following options:
1) Display contents of table
2) Insert new row to table
3) Update a row of the table
4) Delete a row of the table
q) Quit
"""

if __name__ == "__main__":
    while True:
        choice = input(menuText)
        if choice == "q":
            break
        elif choice == "1":
            printTable()
        elif choice == "2":
            insertIntoTable()
        elif choice == "3":
            updateRow()
        elif choice == "4":
            deleteRowFromTable()
        else:
            print("That is not a valid choice.")
            print(menuText)