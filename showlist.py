from pymongo import MongoClient
import certifi

try:
    client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
    db=client["office"]
    coll=db["workers"]
    lst=[]

    doc=coll.find()
    for item in doc:
        lst.append(item)
    print(lst)

except:
    print("No Document Find")