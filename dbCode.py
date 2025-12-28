import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

global CONFESSION_LIMIT
CONFESSION_LIMIT = 5

load_dotenv()
uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['Confessions']
collection = db['Confessions']

# STORE NEW CONFESSION
def StoreNewConfession(ConfessorName, ConfessionData, IP):
    global CONFESSION_LIMIT

    query = {"_id":IP}
    doc = collection.find_one(query)

    if doc == None:
        current_time = datetime.datetime.now(datetime.timezone.utc)
        data = {
            "_id": IP,
            "timestamp" : current_time,
            "ConfessorName" : ConfessorName,
            "ConfessionData" : {
                "1":ConfessionData
            },
            "TimesConfessed": 1
        }

        result = collection.insert_one(data)

        #CHECK IF INSERTED
        if result.acknowledged:
            return {"Value" : True, "Message" : "Data inserted successfully"}
        else:
            return {"Value" : False, "Message" : "Data could not be inserted"}

    else:
        TimesConfessed = doc["TimesConfessed"]
        Confessions = doc["ConfessionData"]

        if TimesConfessed < CONFESSION_LIMIT:
            TimesConfessed += 1
            Confessions.update({str(TimesConfessed) : ConfessionData})
            current_time = datetime.datetime.now(datetime.timezone.utc)
            newvalue = {
                "$set":{
                    "timestamp" : current_time,
                   "ConfessionData" : Confessions,
                   "TimesConfessed" : TimesConfessed
                }
            }
            
            result = collection.update_one(query, newvalue)

            if result.modified_count == 1 and result.acknowledged:
                return {"Value" : True, "Message": "Data updated successfully"}
            else:
                return {"Value" : False, "Message" : "Data could not be updated"}
        
        else:
            return {"Value" : False, "Message" : "Confessions limit reached"}

# RETRIEVE ALL CONFESSIONS
def RetrieveConfessions():
    data = collection.find()
    return list(data)