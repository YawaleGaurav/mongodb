from pymongo import MongoClient
import certifi


client=MongoClient("mongodb+srv://gaurav:9146327025@cluster0.7ud6v.mongodb.net/Bhaibhai?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client["office"]
coll=db["workers"]
dic={}

try:
    id=int(input("Enter Emplyee Id : "))
    dic["_id"]=id

    doc=coll.find_one(dic)
    if doc:
        print(doc)
    else:
        print("No Document Find")

except:
    print("Invalid Input")
