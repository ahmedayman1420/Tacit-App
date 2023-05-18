import os
from pymongo import MongoClient
from dotenv import load_dotenv


class Database:

    def __init__(self):
        '''Inititalize the data base parameters
        and connect to it using provided args

        @Args
            - database_name: The name of the database ex: 'clinic'
        '''

        try:

            # load environment variables
            load_dotenv()

            # Retrieve the connection string from the environment variables
            self.connection_string = os.getenv("CONNECTION_STRING")

            # Connect to the MongoDB server
            self.client = MongoClient(self.connection_string)

            # initialize the database instance
            self.db = None

        
        except Exception:
            print(Exception)


    def connect_db(self, database_name: str):
        '''Connect to database and returns its object

        @Args
            - database_name: The name of the database

        @Returns
            - Database object
        '''

        if not database_name:
            raise Exception('Database name not valid')
    
        if self.db is None:
            self.db = self.client[database_name]
        return self
    

    def connect_collection(self, collection_name: str):
        '''Connect to database collection

        @Args
            - collection_name: The name of the collection/table

        @Returns
            - Object to collection
        '''

        if not collection_name:
            raise Exception('Database Collection Name not valid')
        
        if self.db is None:
            raise Exception('You have to connect to database')
        
        return self.db[collection_name]
    
    def __del__(self):
        self.client.close()