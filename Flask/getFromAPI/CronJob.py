import requests
from pymongo import MongoClient
import pymongo



def get_mongo_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://DipMukeshbahiPatel:Dip141100@cluster0.i0vgfb2.mongodb.net/?retryWrites=true&w=majority"    

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client["final_project"]["final_project"]

def cronJob():
    get_client_instance = get_mongo_database()
   
    url = "https://air-quality.p.rapidapi.com/history/airquality"

    querystring = {"lon":"-78.638","lat":"35.779"}

    headers = {
        "X-RapidAPI-Key": "b1f5ab84dbmsha7fba0b609d912ep1c40f1jsnba06ec843ae9",
        "X-RapidAPI-Host": "air-quality.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)


    Jsonarray = response.json()
    json_data= Jsonarray["data"]
    print(json_data)
    if (len(json_data) >= 10):
        # Getting top most 10 data
        dumpdata = json_data[:10]
        # Creating a variable for indexing
        index = 0
        for i in dumpdata:
            # Inserting data to mongodb client
            get_client_instance.insert_one(i)
            index += 1
    else:
        print("pass")
        pass



if __name__ == '__main__':
    cronJob()