import ConfigParser
from robot.api import logger
from pymongo import mongo_client

class MongoConnectionManager(object):
    """
    Connection Manager handles the connection & disconnection to the database.
    """

    def __init__(self):
        """
        Initializes _dbconnection to None.
        """
        self._dbconnection = None
        
    def connect_to_mongodb(self, dbHost='localhost', dbPort=27017, dbMaxPoolSize=10, dbNetworkTimeout=None, dbDocClass=dict, dbTZAware=False):
        """
        Loads pymongo and connects to the MongoDB host using parameters submitted.
        
        Example usage:
        | # To connect to foo.bar.org's MongoDB service on port 27017 |
        | Connect To MongoDB | foo.bar.org | ${27017} |
        | # Or for an authenticated connection |
        | Connect To MongoDB | admin:admin@foo.bar.org | ${27017} |
        """

        self._dbconnection = mongo_client.MongoClient(host=dbHost, port=int(dbPort), document_class=dbDocClass,
                                                      tz_aware=dbTZAware, maxPoolSize=dbMaxPoolSize,
                                                      socketTimeoutMS=dbNetworkTimeout)

    def disconnect_from_mongodb(self):
        """
        Disconnects from the MongoDB server.
        
        For example:
        | Disconnect From MongoDB | # disconnects from current connection to the MongoDB server | 
        """
        self._dbconnection.close()
