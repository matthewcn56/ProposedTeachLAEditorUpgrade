from inputComponentScraper import getInputComponentList
from propsScraper import getValidProps
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import firebase_admin.db
import json
from dbConfig import config

components = getInputComponentList()

cred = credentials.Certificate(config["configPath"])

default_app = firebase_admin.initialize_app(cred, {
    "databaseURL" : config["databaseURL"]
})
print (default_app.name)

for component in components:
    props = getValidProps(component["componentLink"])

    for prop in props:
        try: 
            path = firebase_admin.db.reference("MaterialUI/" + component["componentName"]+"/validProps/" + prop)
            path.set("exists")
        except ValueError:
            print("Invalid Path!")
        except TypeError:
            print("Invalid Path!")
        except firebase_admin.exceptions.FirebaseError:
            print("Invalid Path!")
        
        