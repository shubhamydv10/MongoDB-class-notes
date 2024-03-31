import pymongo
client = pymongo.MongoClient("mongodb+srv://shubham:shubham1250@shubham.nuxwv7x.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database = client["myinfo"]
collection = database['shub']

#record = collection.find()
#for i in record:
    #print(i)

#data = collection.find({'companyName' : 'iNeuron'})
data = collection.find({"courseOffered" : {"$gt":"E"}})
for i in data:
    print(i)