from turtleMethodsScraper import getTurtleMethodsList
from turtleMethodParameterScraper import getTurtleMethodParametersList
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin.db
import json
from dbConfig import config


cred = credentials.Certificate(config["configPath"])

default_app = firebase_admin.initialize_app(cred, {
    "databaseURL" : config["databaseURL"]
})
print (default_app.name)

methods = getTurtleMethodsList()
for method in methods:
    methodName = method["methodName"]
    try:
        path = firebase_admin.db.reference("Turtle/methods/" +methodName+"/link")
        path.set(method["methodLink"])
        methodParams = getTurtleMethodParametersList(methodName)
        if methodParams is not None:
            for methodParam in methodParams:
                paramPath = firebase_admin.db.reference("Turtle/methods/" +methodName+"/parameters/" 
                +methodParam["name"])
                paramPath.set(methodParam["description"])
    except ValueError:
        print("Invalid Path!")
    except TypeError:
        print("Invalid Path!")
    except firebase_admin.exceptions.FirebaseError:
        print("Invalid Path!")

