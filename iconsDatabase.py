from inputComponentScraper import getInputComponentList
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin.db
import json
from dbConfig import config

icons = getInputComponentList()

cred = credentials.Certificate(config["configPath"])

default_app = firebase_admin.initialize_app(cred, {
    "databaseURL" : config["databaseURL"]
})
print (default_app.name)

for icon in icons:
    try:
        path = firebase_admin.db.reference("MaterialUI/" + icon["componentName"])
        path.set(icon["componentLink"])
    except ValueError:
        print("Invalid Path!")
    except TypeError:
        print("Invalid Path!")
    except firebase_admin.exceptions.FirebaseError:
        print("Invalid Path!")
    


