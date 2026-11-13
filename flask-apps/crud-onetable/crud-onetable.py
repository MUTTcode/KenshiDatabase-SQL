#!/usr/bin/python3
import json
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


with open('secrets.json', 'r') as secretFile:
    creds = json.load(secretFile)['mysqlCredentials']

connection = mysql.connector.connect(**creds)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def showAnimals():
    mycursor = connection.cursor()

    animalName = request.args.get('name')
    organicORrobot = request.args.get('organicORrobot')
    baseMelee = request.args.get('baseMelee')
    baseDefense = request.args.get('baseDefense')
    factionID = request.args.get('factionID')
    
    if animalName is not None:
        mycursor.execute(
            "INSERT INTO animals (name, organicORrobot, baseMelee, baseDefense, factionID) VALUES (%s, %s, %s, %s, %s)", 
            (animalName, organicORrobot, baseMelee, baseDefense, factionID)
        )
        connection.commit()
    elif request.args.get('delete') == 'true':
        deleteID = request.args.get('id')
        mycursor.execute(
            "DELETE FROM animals WHERE animalID=%s;", 
            (deleteID,)
        )
        connection.commit()

    mycursor.execute("SELECT * FROM animals")
    myresult = mycursor.fetchall()
    mycursor.close()
    return render_template('animals-list.html', collection=myresult)

@app.route("/updateAnimals")
def updateAnimals():
    id = request.args.get('id')
    animalName = request.args.get('name')
    organicORrobot = request.args.get('organicORrobot')
    baseMelee = request.args.get('baseMelee')
    baseDefense = request.args.get('baseDefense')
    factionID = request.args.get('factionID')
    if id is None:
        return "Error, id not specified"
    elif animalName is not None:
        mycursor = connection.cursor()
        mycursor.execute(
            "UPDATE animals SET name=%s, organicORrobot=%s, baseMelee=%s, baseDefense=%s, factionID=%s WHERE animalID=%s;", 
            (animalName, organicORrobot, baseMelee, baseDefense, factionID, id)
        )
        mycursor.close()
        connection.commit()
        return redirect(url_for('showAnimals'))

    mycursor = connection.cursor()
    mycursor.execute(
        "SELECT name, organicORrobot, baseMelee, baseDefense, factionID FROM animals WHERE animalID=%s;", 
        (id,)
    )
    existingName, existingOrgRob, existingMelee, existingDef, existingFacID = mycursor.fetchone()
    mycursor.close()
    return render_template(
        'animals-update.html', id=id, existingName=existingName, existingOrgRob=existingOrgRob,
        existingMelee=existingMelee, existingDef=existingDef, existingFacID=existingFacID
    )


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")