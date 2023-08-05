from pymongo import MongoClient
user = 'avinash'
password = '123'
host='localhost'

connecturl = "mongodb://{}:{}@{}:27017/?authSource=admin".format(user,password,host)


print("Connecting to mongodb server")
connection = MongoClient(connecturl)


print("Getting list of databases")
dbs = connection.list_database_names()


for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")

connection.close()