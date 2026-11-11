#!/usr/bin/python3

from flask import Flask, render_template, request
import mysql.connector, os
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def showSpeakers():
    with open('secrets.json', 'r') as secretFile:
        creds = json.load(secretFile)['mysqlCredentials']

    connection = mysql.connector.connect(**creds)
    mycursor = connection.cursor()

    # If there is a name and desc 'GET' variable, insert the new value into the database
    nameNEW = request.args.get('name')
    organicORrobotNEW = request.args.get('organicORrobot')
    baseMeleeNEW = request.args.get('baseMelee')
    baseDefenseNEW = request.args.get('baseDefense')
    factionIDNEW = request.args.get('factionID')

    if nameNEW is not None:
        mycursor.execute(
            f"INSERT INTO animals" 
            f"(name, organicORrobot, baseMelee," 
            f"baseDefense, factionID) values (%s, %s, %s, %s, %s)", 
            (nameNEW, organicORrobotNEW, baseMeleeNEW, baseDefenseNEW, factionIDNEW)
        )
        connection.commit()
    
    # Fetch the current values of the speaker table
    mycursor.execute(
        f"Select animalID, name, organicORrobot," 
        f"baseMelee, baseDefense, factionID FROM animals"
    )
    myresult = mycursor.fetchall()
    mycursor.close()
    connection.close()
    return render_template('animal-list.html', collection=myresult)
    #return "Hello world"


if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")