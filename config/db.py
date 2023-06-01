# Import pymongo
from pymongo import MongoClient

# Create a class for the database


class Database:
    # Create a function to connect to the database
    def connect(self):
        # Create a variable for the client
        client = MongoClient(
            "mongodb+srv://thenowrock:UTDFdaXkbt98WtcD@first-db-mongo.bxhdjct.mongodb.net/?retryWrites=true&w=majority")
        # Create a variable for the database
        db = client["JUGUETERIAJJJ"]
        
        # Return the database
        return db

# Create a variable for the database
db = Database().connect()